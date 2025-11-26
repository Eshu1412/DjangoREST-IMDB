from rest_framework import serializers
from watchapp.models import WatchList,StreamPlatForm,Review


class StreamPlatFormSerializer(serializers.ModelSerializer):
    watchlist=serializers.HyperlinkedRelatedField(
        many=True,
        view_name='watch-detail',
        read_only=True,
    )
    class Meta:
        model=StreamPlatForm
        fields="__all__"
        extra_kwargs={
            'url':{
                "view_name":"stream-list",
                "lookup_field": "pk"
            }
        }
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
      
class WatchListSerializer(serializers.ModelSerializer):
    review=ReviewSerializer(many=True,read_only=True)
    platform=StreamPlatFormSerializer(read_only=True)
    class Meta:
        model=WatchList
        fields="__all__"
