from rest_framework.serializers import ModelSerializer
from .models import NewsLink, Startup, Tag   

class TagSerializer(ModelSerializer):
   
   class Meta:
       model = Tag
       fields = "__all__"

class StartupSerializer(ModelSerializer):
    
    tags = TagSerializer(many=True)

    class Meta:
       model = Startup
       fields = "__all__"

class NewsLinkSerailzer(ModelSerializer):

    startup = StartupSerializer

    class Meta:
       model = NewsLink
       fields = "__all__"