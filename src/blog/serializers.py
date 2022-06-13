from rest_framework.serializers import ModelSerializer

from organizer.serializers import (
    StartupSerializer,
    TagSerializer,
)

from .models import Post


class PostSerializer(ModelSerializer):
    """Serialize Post data"""

    tags = TagSerializer(many=True)
    startups = StartupSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
