from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.views.decorators.http import require_safe
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from .models import NewsLink, Startup, Tag
from .serializers import (
    NewsLinkSerialzer,
    StartupSerializer, 
    TagSerializer
)

@require_safe
def tag_list(request):
    tag_list = Tag.objects.all()
    template = loader.get_template("tag/list.html")
    # tag_list is the varialbe referenced in the template
    context = {"tag_list": tag_list} 
    html_content = template.render(context)
    return HttpResponse(html_content)

@require_safe
def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    template = loader.get_template("tag/detail.html")
    context = {"tag": tag}
    html_content = template.render(context)
    return HttpResponse(html_content)

class TagApiDetail(RetrieveAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"


class TagApiList(ListAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class StartupApiDetail(RetrieveAPIView):

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"


class StartupApiList(ListAPIView):

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

class NewsLinkApiDetail(RetrieveAPIView):

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerialzer

    def get_object(self):
        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug
        )
        self.check_object_permissions(
            self.request, newslink
        )
        return newslink

class NewsLinkApiList(ListAPIView):

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerialzer