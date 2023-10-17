from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import File
from .serializers import FileSerializer


class FileViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = File.objects.all().order_by("-id")
    serializer_class = FileSerializer
    http_method_names = ["get", "post"]

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
