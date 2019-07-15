from rest_framework import serializers
from .models import Uploads


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploads
        fields = "__all__"
