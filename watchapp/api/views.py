from rest_framework.views import APIView
from watchapp.models import StreamPlatForm,WatchList,Review
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics
from watchapp.api.serializers import (StreamPlatFormSerializer,
                                      ReviewSerializer,
                                      WatchListSerializer)


#APIView based class
class WatchListAV(APIView):
    def get(self,request):
        watch=WatchList.objects.all()
        serializer=WatchListSerializer(watch,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class WatchListDetailAV(APIView):
    def get(self,request,pk):
        try:
            watch=WatchList.objects.get(pk=pk)
            serializer=WatchListSerializer(watch)
        except WatchList.DoesNotExist:
            return Response({'message':"Movie with this id is not associated"})
        return Response()
class WatchListAV(APIView):
    def get(self,request,pk=None):
        if pk==None:
            watch=WatchList.objects.all()
            serializer=WatchListSerializer(watch,many=True,context={'request': request} )
        else:
            try:
                watch=WatchList.objects.get(pk=pk)
                serializer=WatchListSerializer(watch,many=False,context={'request': request})
            except WatchList.DoesNotExist:
                return Response({"message":"The provided movie id does not exists"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
class StreamPlatformAV(APIView):
     def get(self,request,pk=None):
         if pk==None:
            streamplatform=StreamPlatForm.objects.all()
            serializer=StreamPlatFormSerializer(streamplatform,many=True,context={'request': request})
         else:
             try:
                 streamplatform=StreamPlatForm.objects.get(pk=pk)
                 serializer=StreamPlatFormSerializer(streamplatform,many=False,context={'request': request})
             except StreamPlatForm.DoesNotExist:
                 return Response({'message': 'Stream Platform id does not exist'})
         return Response(serializer.data)
     def post(self,request):
         serializer=StreamPlatFormSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
         else:
             return Response(serializer.errors)
         return Response(serializer.data)
#####################################################################################################################################
#Generics
class ReviewList(generics.ListCreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
class ReviewDetail(generics.RetrieveDestroyAPIView):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        pk=self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)
#Mixins and Generic View based class

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    

######################################################################################################################################