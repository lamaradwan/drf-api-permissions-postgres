from rest_framework import serializers
from api.models import Quote, Post


class QuotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
