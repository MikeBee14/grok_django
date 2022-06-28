from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    NewsLinkApiDetail,
    NewsLinkApiList,
    StartupApiDetail,
    StartupApiList,
    TagApiList, 
    TagApiDetail
)
from .viewsets import TagViewSet

api_router = SimpleRouter()
api_router.register("tag", TagViewSet, base_name="api-tag")
api_routes = api_router.urls

urlpatterns = api_routes + [
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