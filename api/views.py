from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from django.db.models import *
from django.db.models.functions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from api.constants.constant_method import read_json_file
from paintwaleapp.models import *
from random import randint


class Login(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.login_json = json_data['login']

    def post(self, request):
        try:
            post_data = request.data
            users = Users.objects.filter(phone=post_data['phone'])
            if users.exists():
                user = users[0]
                if post_data['mode'] == 'otp':
                    user.otp = randint(1111,9999)
                    user.save()
                    return Response({'message': self.login_json['otp_sent'],'otp': user.otp},status=status.HTTP_200_OK)
                elif post_data['mode'] == 'verify':
                    if user.otp == int(post_data['otp']):
                        user.otp = None
                        user.save()
                        users = users.values().get()
                        token = RefreshToken.for_user(user=user)
                        users['token'] = str(token.access_token)
                        users['refresh_token'] = str(token)
                        return Response(users,status=status.HTTP_200_OK)
                    else:
                        return Response({'message': self.login_json['invalid_otp']},status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({'message': self.login_json['key_missing']},status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'message': self.login_json['no_user_found']},status=status.HTTP_401_UNAUTHORIZED)
            pass
        except Users.DoesNotExist:
            return Response({'message': self.login_json['no_user_found']},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'message': self.login_json['invalid_credentials']},status=status.HTTP_401_UNAUTHORIZED)

class RoomTypeList(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.room_type = json_data['common_message']
    
    def get(self, request):
        try:
            rooms = RoomType.objects.filter(active=True).values_list('room_type',flat=True).distinct()
            return Response({'rooms': rooms},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.room_type['error']},status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        try:
            post_data = request.data
            RoomType.objects.create(room_type=post_data['room_name'],active=True)
            return Response({'message': self.room_type['creating']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.room_type['error_creating']},status=status.HTTP_401_UNAUTHORIZED)

class WallsList(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.walls = json_data['common_message']
    
    def get(self, request):
        try:
            walls = Walls.objects.filter(active=True).values_list('wall_name',flat=True).distinct()
            return Response({'walls': walls},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.walls['error']},status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        try:
            post_data = request.data
            Walls.objects.create(wall_name=post_data['wall_name'])
            return Response({'message': self.walls['creating']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.walls['error_creating']},status=status.HTTP_401_UNAUTHORIZED)

class ProcessProduct(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.processproduct = json_data['common_message']
    
    def get(self, request):
        try:
            process = Process.objects.filter(active=True).values('id','name','servicetype_id','servicetype__service_name')
            product = Product.objects.filter(active=True).values('id','name','product_type','product_category','brand_id','brand__brand_name','servicetype_id','servicetype__service_name')
            return Response({'process': process, 'product': product},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.processproduct['error']},status=status.HTTP_401_UNAUTHORIZED)

class CityList(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.cityresponse = json_data['common_message']
    
    def get(self, request):
        try:
            cities = City.objects.filter(active=True).values('id','city_name','city_code').distinct()
            return Response(cities, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.cityresponse['error']},status=status.HTTP_401_UNAUTHORIZED)
    
class CreateLead(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.lead = json_data['lead']
    
    def get(self, request):
        try:
            leads = Lead.objects.filter(status__in=[PENDING,MEASUREMENT_DONE,QUOTATION_SENT,RESCEDULE,CALLBACKREQUESTED]).values()
            return Response(leads,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.lead['error_fetching']},status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        try:
            user_id = get_userId_from_access_token(request)
            post_data = request.data
            leads = Lead.objects.filter(phone__icontains=post_data['phone'],lead_date=datetime.now().date())
            if leads.exists():
                return Response({'message': self.lead['lead_exists']},status=status.HTTP_200_OK)
            
            leads = Lead.objects.filter(phone__icontains=post_data['phone'],status__in=[PENDING,MEASUREMENT_DONE])
            if leads.exists():
                lead = leads[0]
            else:
                lead = Lead()
                lead.created_at = datetime.now()
                lead.lead_date = datetime.now().date()
                lead.lead_time = datetime.now().time()
            
            lead.name = post_data.get('name',None)
            lead.phone = post_data.get('phone',None)
            lead.city_id = post_data.get('city_id',None)
            lead.alternate_phone = post_data.get('alternate_phone',None)
            lead.email = post_data.get('email',None)
            lead.status = post_data.get('status',PENDING)
            lead.landmark = post_data.get('landmark',None)
            if post_data.get('visit_date_time',None):
                lead.visit_date_time = datetime.strptime(post_data['visit_date_time'],'%Y-%m-%d %H:%M')
            
            if post_data.get('re_schedule_time',None):
                lead.re_schedule_time = datetime.strptime(post_data['re_schedule_time'],'%Y-%m-%d %H:%M')
            
            lead.channel = post_data.get('channel',None)
            lead.channel_reference = post_data.get('channel_reference',None)
            lead.project_type = post_data.get('project_type',None)
            lead.house_type = post_data.get('house_type',None)
            lead.address = post_data.get('address',None)
            lead.remarks = post_data.get('remarks',None)
            lead.updated_at = datetime.now()
            lead.updated_by_id = user_id
            lead.save()
            return Response({'message': self.lead['created']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.lead['error']},status=status.HTTP_401_UNAUTHORIZED)