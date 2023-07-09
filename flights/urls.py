from django.urls import path
# from .views import ClubList, ClubDetail



urlpatterns = [
    path('v1/events/', ClubList.as_view(), name='event_detail'),
    path('<int:pk>/', ClubDetail.as_view(), name='club_detail'),
]