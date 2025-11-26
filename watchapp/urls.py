from django.urls import path
from watchapp.api import views
urlpatterns = [
    path('',views.WatchListAV.as_view(),name='watch-list'),
    path('<int:pk>/',views.WatchListAV.as_view(),name='watch-detail'),
    path('stream/',views.StreamPlatformAV.as_view(),name='streamplatform'),
    path('stream/<int:pk>/',views.StreamPlatformAV.as_view(),name='stream-list'),
    path('review/',views.ReviewList.as_view(),name='review-movie'),
    path('review/<int:pk>/',views.ReviewDetail.as_view(),name='review-detail'),

    path('stream/<int:pk>/review',views.ReviewDetail.as_view(),name='streampalform'),
    path('stream/review/<int:pk>',views.ReviewList.as_view()),
    
 ]
