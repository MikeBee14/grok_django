from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import NewsLink, Startup, Tag   

class TagSerializer(ModelSerializer):
   
   class Meta:
       model = Tag
       fields = "__all__"

class StartupSerializer(HyperlinkedModelSerializer):
    
    tags = TagSerializer(many=True)

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

    startup = StartupSerializer

    class Meta:
       model = NewsLink
       fields = "__all__"