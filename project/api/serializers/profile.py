from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'city']
        model = User