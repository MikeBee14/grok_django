from rest_framework.viewsets import ModelViewSet

from .models import Tag
from .serializers import TagSerializer

class TagViewSet(ModelViewSet):

    lookup_field = "slug"
    queryset = Tag.objects.all()
    serializer_class = Tag