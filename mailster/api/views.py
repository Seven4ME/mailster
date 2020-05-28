from rest_framework import generics
from rest_framework.response import Response
from .seriallizers import EmailOpenSerializer
from email_import.models import Sending
# Create your views here.
class PixelView(generics.CreateAPIView):
    serializer_class = EmailOpenSerializer
    lookup_url_kwarg = "uuid"

    def get(self, request, **kwargs):
        uuid = self.kwargs.get(self.lookup_url_kwarg)
        is_existing_uuid = Sending.objects.filter(uuid=uuid).exists()

        if is_existing_uuid == True:
            sending_obj = Sending.objects.get(uuid=uuid)
            sending_obj.is_opened = True
            sending_obj.save()
        else:
            is_existing_uuid = 'UUID: {} does not exists in db'.format(uuid)
        return Response(is_existing_uuid)