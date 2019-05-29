from rest_framework import generics, permissions
from show.models import Show
from show.serializers import ShowSerializer

class ShowView(generics.ListCreateAPIView):

    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = (permissions.AllowAny,)

class ShowIDView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = (permissions.AllowAny,)
