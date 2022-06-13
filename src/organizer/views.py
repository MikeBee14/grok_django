from django.shortcuts import (get_list_or_404, get_object_or_404)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Startup, Tag
from .serializers import StartupSerializer, TagSerializer

class TagApiDetail(APIView):

    def get(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        s_tag = TagSerializer(tag)
        return Response(s_tag.data)


class TagApiList(APIView):

    def get(self, request):
        tag_list = get_list_or_404(Tag)
        s_tag = TagSerializer(tag_list, many=True)
        return Response(s_tag.data)

class StartupApiDetail(APIView):

    def get(self, request, slug):
        startup = get_object_or_404(Tag, slug=slug)
        s_startup = StartupSerializer(
            startup, context={"request": request}
        )
        return Response(s_startup.data)


class StartupApiList(APIView):

    def get(self, request):
        startup_list = get_list_or_404(Startup)
        s_startup = StartupSerializer(
            startup_list, 
            many=True,
            context={"request": request}
        )
        return Response(s_startup.data)