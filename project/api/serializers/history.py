from rest_framework import validators
from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault, ImageField

from ..models import History, HistoryImage
from .base import BaseSerializer
from .profile import MentorSerializer


class HistoryImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='image.id')
    image = serializers.ImageField(source='image.image')
    image_caption = serializers.CharField(source='image.image_caption')

    class Meta:
        fields = ['id', 'image', 'image_caption']
        model = HistoryImage


class HistorySerializer(BaseSerializer):
    mentor = MentorSerializer(default=CurrentUserDefault())
    image = ImageField()
    images = HistoryImageSerializer(many=True)

    class Meta(BaseSerializer.Meta):
        tags = None
        model = History
        validators = [
            validators.UniqueTogetherValidator(
                queryset=History.objects.all(),
                fields=['mentor', 'child'],
                message='Такая пара наставник - ребенок уже добавлена'
            )
        ]
