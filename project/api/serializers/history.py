from rest_framework import serializers
from rest_framework.serializers import ImageField

from ..models import History, HistoryImage
from .profile import MentorSerializer


class HistoryImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='image.id')
    image = serializers.ImageField(source='image.image', use_url=False)
    image_caption = serializers.CharField(source='image.image_caption')

    class Meta:
        fields = ['id', 'image', 'image_caption']
        model = HistoryImage


class HistorySerializer(serializers.ModelSerializer):
    mentor = MentorSerializer()
    image = ImageField(use_url=False)
    images = HistoryImageSerializer(many=True)

    class Meta:
        model = History
        exclude = ['output_to_main', 'image_url']
