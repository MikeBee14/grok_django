from django.urls import path

from .views import (
    PostApiDetail,
    PostApiList)

urlpatterns = [
    path("blog/", PostApiList.as_view(), name="api-post-list"),
    path(
        "blog/<int:year>/<int:month>/<str:slug>/", 
        PostApiDetail.as_view(), 
        name="api-post-detail"),
]