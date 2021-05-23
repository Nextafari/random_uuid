import uuid
import datetime
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import RandomId
from .serializers import RandomIdSerializer


class RandomUUID(APIView):
    """class for the randomly generated UUID"""
    permission_classes = [AllowAny]
    def get(self, request):
        random_id = uuid.uuid4()
        today = str(datetime.datetime.now())
        RandomId.objects.create(
            random_uuid=random_id.hex,
            time_created=today
        )
        date_time = RandomId.objects.values_list(
            "time_created", "random_uuid"
        ).order_by("-time_created")
        print(random_id.hex)
        return Response(
            dict(date_time)
        )

