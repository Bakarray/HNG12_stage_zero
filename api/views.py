from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timezone

# Create your views here.
class InfoObject(APIView):
    def get(self, request, format=None):
        email = "poesitor1@gmail.com"
        github_url = "https://github.com/Bakarray/HNG12/Task1"
        current_datetime = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
        
        data = {
            "email": email,
            "current_datetime": current_datetime,
            "github_url": github_url
        }

        return Response(data)