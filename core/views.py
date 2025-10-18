from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from decouple import config
import requests
import logging  
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)
@method_decorator(ratelimit(key='ip', rate='100/h', method='GET'), name='get')
class MeView(APIView):
    
    logger.info("Profile endpoint accessed")
    
    
    def get(self, request):

        # Rate Limit
        if getattr(request, 'limited', False):
            return Response({"error": "Rate limit exceeded. Try again later."}, status=status.HTTP_429_TOO_MANY_REQUESTS)
            



        timestamp = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
        api_status = status.HTTP_200_OK

        # Retrieving the cat fact
        cat_fact = ""
        try:
            r = requests.get('https://catfact.ninja/fact', timeout=5)
            if r.status_code == 200:
                data = r.json()
                if 'fact' in data:
                    cat_fact = data['fact']
                    logger.info("Fact retrieved successfully")
            else:
                cat_fact = "Could not fetch cat fact right now."
                api_status = status.HTTP_503_SERVICE_UNAVAILABLE
                logger.error(f"couldn't fetch cat fact {r.status_code}")
        except requests.exceptions.Timeout:
            cat_fact = "The server took too long to respond."
            api_status = status.HTTP_503_SERVICE_UNAVAILABLE
            logger.error("Request timed out")
        except requests.exceptions.RequestException:
            cat_fact = "Something went wrong while fetching the fact."
            api_status = status.HTTP_503_SERVICE_UNAVAILABLE
            logger.error("Request exception occurred")
        except Exception:
            cat_fact = "An unexpected error occurred."
            api_status = status.HTTP_500_INTERNAL_SERVER_ERROR  
            logger.error("Unexpected error")

        # Data Response
        data = {
            "status": "success" if api_status == status.HTTP_200_OK else "error",
            "user": {
                "email": config('EMAIL'),
                "name": config('NAME'),
                "stack": "Python/Django"
            },
            "timestamp": timestamp,
            "fact": cat_fact
        }

        return Response(data, status=api_status)

