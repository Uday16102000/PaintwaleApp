
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.Login.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('processproduct/', views.ProcessProduct.as_view(),name='processproduct'),
    path('walls/', views.WallsList.as_view(),name='walls'),
    
    
]