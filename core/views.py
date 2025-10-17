from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from decouple import config
import requests

class MeView(APIView):
    
    def get(self, request):
        now = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
        api_status = status.HTTP_200_OK

        cat_fact = "Cats are amazing creatures."
        try:
            r = requests.get('https://catfact.ninja/fact', timeout=5)
            if r.status_code == 200:
                data = r.json()
                if 'fact' in data:
                    cat_fact = data['fact']
            else:
                cat_fact = "Could not fetch cat fact right now."
                api_status = status.HTTP_503_SERVICE_UNAVAILABLE
        except requests.exceptions.Timeout:
            cat_fact = "The cat fact service took too long to respond."
            api_status = status.HTTP_503_SERVICE_UNAVAILABLE
        except requests.exceptions.RequestException:
            cat_fact = "Something went wrong fetching the cat fact."
            api_status = status.HTTP_503_SERVICE_UNAVAILABLE
        except Exception:
            cat_fact = "An unexpected error occurred."
            api_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = {
            "status": "success" if api_status == status.HTTP_200_OK else "error",
            "user": {
                "email": config('MY_EMAIL'),
                "name": config('MY_NAME'),
                "stack": "Python/Django"
            },
            "timestamp": now,
            "fact": cat_fact
        }

        return Response(data, status=api_status)

