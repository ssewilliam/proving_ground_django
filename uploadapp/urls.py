from django.urls import path
from .views import (UploadView,)

app_name = 'uploadapp'
urlpatterns = [
    path('', UploadView.as_view())
]
