from django.urls import path

from .views import FileViewSet


urlpatterns = [
    path("upload/", FileViewSet.as_view({"post": "create"}), name="upload_file"),
    path("files/", FileViewSet.as_view({"get": "list"}), name="list_files"),
]
