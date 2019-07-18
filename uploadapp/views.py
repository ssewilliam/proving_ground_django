from django.shortcuts import get_list_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, CreateAPIView
)
from rest_framework import status
from .serializer import UploadSerializer
from .models import Uploads


class UploadView(CreateAPIView, ListAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = UploadSerializer

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        all_uploads = get_list_or_404(
            Uploads
        )
        return all_uploads
