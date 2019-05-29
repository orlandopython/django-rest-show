from rest_framework import serializers
from show.models import Show

class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = ('id', 'name', 'network', 'rating')