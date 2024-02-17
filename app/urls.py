from django.urls import path
from .views import UploadView, ListView

urlpatterns = [
    path('api/upload/', UploadView.as_view(), name='Upload'),
    path('api/files/', ListView.as_view(), name='List')
]
