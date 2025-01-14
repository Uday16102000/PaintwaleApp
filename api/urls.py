
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.Login.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('processproduct/', views.ProcessProduct.as_view(),name='processproduct'),
    path('room_list/', views.RoomTypeList.as_view(),name='room_list'),
    path('wall_list/', views.WallsList.as_view(),name='wall_list'),
    path('city_list/', views.CityList.as_view(),name='city_list'),
    path('create_lead/', views.CreateLead.as_view(),name='create_lead'),
    path('create_measurement/', views.CreateMeasurement.as_view(),name='create_measurement'),
    path('measurement/<int:lead_id>/', views.CreateMeasurement.as_view(),name='measurement'),
    path('create_quotation/', views.CreateQuotation.as_view(),name='create_quotation'),
    path('quotation/<int:quotation_id>/', views.CreateQuotation.as_view(),name='quotation'),
    path('create_price_entry/', views.CreatePrice.as_view(),name='create_price_entry'),
    path('view_quotation/<int:quotation_id>/', views.ViewQuotation.as_view(),name='view_quotation_get'),
    path('view_quotation/', views.ViewQuotation.as_view(),name='view_quotation'),
    
    
    
    
]