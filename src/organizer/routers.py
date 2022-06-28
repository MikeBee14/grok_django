from django.urls import path

from .views import (
    NewsLinkApiDetail,
    NewsLinkApiList,
    StartupApiDetail,
    StartupApiList,
    TagApiList, 
    TagApiDetail
)
from .viewsets import TagViewSet

tag_create_list = TagViewSet.as_view(
    {"get": "list", "post": "create"}
)

tag_retrieve_update_delete = TagViewSet.as_view(
    {
        "get": "retreive", 
        "put": "update",
        "patch": "partial_update", 
        "delete": "delete"
    }
)

urlpatterns = [
    path("tag/", tag_create_list, name="api-tag-list"),
    path(
        "tag/<str:slug>/", 
        tag_retrieve_update_delete, 
        name="api-tag-detail"),
    path("startup/", StartupApiList.as_view(), name="api-startup-list"),
    path(
        "startup/<str:slug>/", 
        StartupApiDetail.as_view(), 
        name="api-startup-detail"),
    path("newslink/", NewsLinkApiList.as_view(), name="api-newslink-list"),
    path(
        "newslink/<str:strartup_slug>/<str:newslink_slug>/", 
        NewsLinkApiDetail.as_view(), 
        name="api-newslink-detail"),
]