
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.Login.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('processproduct/', views.ProcessProduct.as_view(),name='processproduct'),
    path('room_list/', views.RoomTypeList.as_view(),name='room_list'),
    path('wall_list/', views.WallsList.as_view(),name='wall_list'),
    
    
]