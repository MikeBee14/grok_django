from rest_framework.relations import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer, 
    HyperlinkedRelatedField, 
    ModelSerializer, 
    SerializerMethodField,
)

from .models import NewsLink, Startup, Tag   

class TagSerializer(ModelSerializer):
   
   class Meta:
       model = Tag
       fields = "__all__"

class StartupSerializer(HyperlinkedModelSerializer):
    
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
       model = Startup
       fields = "__all__"
       extra_kwargs = {
           "url":{
               "lookup_field": "slug",
               "view_name": "api-startup-detail"
        }       
    }

class NewsLinkSerialzer(ModelSerializer):

    url = SerializerMethodField()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="api-startup-detail"
    )

    class Meta:
       model = NewsLink
       exclude = ("id",)
    
    def get_url(self, newslink):
        return reverse(
            "api-newslink-detail",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug
            ),
            request=self.context["request"]
        )