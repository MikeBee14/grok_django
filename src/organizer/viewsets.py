from django.shortcuts import get_object_or_404
from rest_framework.response import Response 
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ViewSet

from .models import Tag
from .serializers import TagSerializer

class TagViewSet(ViewSet):

    def list(self, request):
        tag_list = Tag.objects.all()
        s_tag = TagSerializer(
            tag_list,
            many=True,
            context={"request": request},
        )
        return Response(s_tag.data)

    def retrieve(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = TagSerializer(
            tag,
            context={"request": request},
        )
        return Response(s_tag.data)

    def create(self, request):
        s_tag = TagSerializer(
            data=request.data,
            context={"request": request},
        )
        if s_tag.isvalid():
            s_tag.save()
        return Response(s_tag.data, status=HTTP_201_CREATED)

    def update(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = TagSerializer(
            tag,
            data=request.data,
            context={"request": request},
        )
        if s_tag.isvalid():
            s_tag.save()
            return Response(s_tag.data)
        return Response(s_tag.errors, status=HTTP_400_BAD_REQUEST)

    def partial_update(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = TagSerializer(
            tag,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if s_tag.isvalid():
            s_tag.save()
            return Response(s_tag.data)
        return Response(s_tag.errors, status=HTTP_400_BAD_REQUEST)

    