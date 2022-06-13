from django.urls import path

from .views import (
    StartupApiDetail,
    StartupApiList,
    TagApiList, 
    TagApiDetail
)

urlpatterns = [
    path("tag/", TagApiList.as_view(), name="api-tag-list"),
    path(
        "tag/<str:slug>/", 
        TagApiDetail.as_view(), 
        name="api-tag-detail"),
    path("startup/", StartupApiList.as_view(), name="api-startup-list"),
    path(
        "startup/<str:slug>/", 
        StartupApiDetail.as_view(), 
        name="api-startup-detail"),
]