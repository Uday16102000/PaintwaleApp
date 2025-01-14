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
from django.db import transaction
from collections import Counter
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
                        # user.otp = None
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
            rooms = RoomType.objects.filter(active=True).values('id','room_type').distinct()
            return Response(rooms,status=status.HTTP_200_OK)
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
            leads = Lead.objects.filter(status__in=[PENDING,MEASUREMENT_DONE,QUOTATION_SENT,RESCEDULE,CALLBACKREQUESTED]).values().annotate(
                city_name = F('city__city_name')
            )
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

class CreateMeasurement(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.measurement = json_data['measurement']
    
    def get(self, request,lead_id):
        try:
            rooms = Room.objects.filter(lead_id=lead_id).values('id','roomtype_id','roomtype__room_type').distinct()
            for room in rooms:
                room['walls'] = Wall.objects.filter(room_id=room['id']).values('id','wall_type','add_area','sub_area','total_area').distinct()
            return Response(rooms,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.measurement['error_fetching']},status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        try:
            post_data = request.data
            with transaction.atomic():
                for key, value in post_data['details'].items():
                    keys = key.split('|')
                    try:
                        room = Room.objects.get(id=keys[0],lead_id=post_data['lead_id'])
                    except:
                        room = Room.objects.create(lead_id=post_data['lead_id'],roomtype_id=keys[1],created_at=datetime.now())

                    for val in value:
                        walls = Wall.objects.filter(id=val['wall_id'])
                        if walls.exists():
                            wall = walls[0]
                        else:
                            wall = Wall()
                            wall.created_at = datetime.now()
                            
                        wall.room_id = room.id
                        wall.wall_type = val['wall_type'].lower()
                        wall.add_area = val['add_area']
                        wall.sub_area = val['sub_area']
                        wall.total_area = val['total_area']
                        wall.save()
                        
            return Response({'message': self.measurement['created']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.measurement['error']},status=status.HTTP_401_UNAUTHORIZED)

class CreatePrice(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.price_entry = json_data['price_entry']
    
    def post(self, request):
        try:
            user_id = get_userId_from_access_token(request)
            post_data = request.data
            price_list = PriceList.objects.filter(process_id=post_data['process_id'],product_id=post_data['product_id'],city_id=post_data['city_id'])

            if price_list.exists():
                price_list = price_list[0]
            else:
                price_list = PriceList()
                price_list.created_at = datetime.now()
                price_list.created_by_id = user_id
            
            price_list.process_id = post_data['process_id']
            price_list.product_id = post_data['product_id']
            price_list.city_id = post_data['city_id']
            price_list.price = post_data['price']
            price_list.is_lumpsum_rate = post_data.get('is_lumpsum_rate',0)
            price_list.updated_at = datetime.now()
            price_list.updated_by_id = user_id
            price_list.save()
            
            return Response({'message': self.price_entry['created']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.price_entry['error']},status=status.HTTP_401_UNAUTHORIZED)

def create_quotation(post_data,user_id,view_quotation=False):
    quotation = Quotation.objects.filter(id=post_data['quotation_id'])
    if not view_quotation and quotation.exists():
        quotation = quotation[0]
    else:
        quotation = Quotation.objects.create(
            lead_id = post_data['lead_id'],
            brand_id = None,
            quotation_value = None,
            discount = None,
            status = 0,
            accepted_at = None,
            created_at = datetime.now(),
            created_by_id = user_id,
            updated_at = datetime.now(),
            updated_by_id = user_id
        )
    return quotation

def update_qutation_value(quotation,user_id):
    lead_id = quotation.lead_id
    total = QuotationItem.objects.filter(quotation_id=quotation.id).aggregate(total=Sum('total_price'))['total'] or 0
    brands = Counter(list(QuotationItem.objects.filter(quotation_id=quotation.id).exclude(product__brand_id=None).values_list('product__brand_id',flat=True)))
    quotation.quotation_value = total
    quotation.brand_id = brands.most_common(1)[0][0] if len(brands) != 0 else None
    quotation.updated_at = datetime.now()
    quotation.updated_by_id = user_id
    quotation.save()
    
    final_quotation = FinalQuotation.objects.filter(lead_id=lead_id)
    if final_quotation.exists():
        final_quotation = final_quotation[0]
    else:
        final_quotation = FinalQuotation()
        final_quotation.created_at = datetime.now()
        final_quotation.created_by_id = user_id
    
    final_quotation.lead_id = lead_id
    final_quotation.brand_id = quotation.brand_id
    final_quotation.quotation_id = quotation.id
    final_quotation.quotation_value = quotation.quotation_value
    final_quotation.discount = quotation.discount
    final_quotation.updated_at = datetime.now()
    final_quotation.updated_by_id = user_id
    final_quotation.save()
    
    if final_quotation.status in [1,3]:
        Quotation.objects.filter(lead_id=lead_id,status=3).update(status=0,accepted_at=None)
        Quotation.objects.filter(lead_id=lead_id,status__in=[1,2]).update(status=3)
        quotation.status = 1
        quotation.accepted_at = datetime.now()
        quotation.save()
    return final_quotation

class CreateQuotation(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.quotation = json_data['quotation']
    
    def get(self, request, quotation_id):
        try:
            quotation = Quotation.objects.get(id=quotation_id)
            rooms = QuotationItem.objects.filter(quotation_id=quotation.id).values('wall__room__id').annotate(
                room_name = F('wall__room__roomtype__room_type')
            ).distinct()
            for val in rooms:
                quotation_items = QuotationItem.objects.filter(quotation_id=quotation.id,wall__room__id=val['wall__room__id']).values(
                    'id','process_id','product_id','wall_id','total_area','wall_type','price','total_price'
                    ).annotate(
                    process_name = F('process__name'),
                    product_name = F('product__name')
                )
                val['walls'] = quotation_items
            return Response({ 'rooms': rooms, 'quotation_id': quotation.id,'city_id': quotation.lead.city_id },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.quotation['error_fetching']},status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        try:
            post_data = request.data
            user_id = get_userId_from_access_token(request)
            lead = Lead.objects.get(id=post_data['lead_id'])
            city_id = lead.city_id
            with transaction.atomic():
                quotation = create_quotation(post_data, user_id)
                for key, value in post_data['details'].items():
                    keys = key.split('|')
                    try:
                        room = Room.objects.get(id=keys[0],lead_id=post_data['lead_id'])
                    except:
                        room = Room.objects.create(lead_id=post_data['lead_id'],roomtype_id=keys[1],created_at=datetime.now())

                    for val in value:
                        price_entry = PriceList.objects.filter(process_id=val['process_id'],product_id=val['product_id'],city_id=city_id)
                        if price_entry.exists():
                            price_entry = price_entry[0]
                        else:
                            process = Process.objects.get(id=val['process_id'])
                            product = Product.objects.get(id=val['product_id'])
                            raise ValueError({ 'message': self.quotation['price_missing'], 'process_id': val['process_id'],'product_id': val['product_id'],'city_id': city_id,'process': process.name, 'product': product.name })
                        walls = Wall.objects.filter(id=val['wall_id'])
                        if walls.exists():
                            wall = walls[0]
                        else:
                            wall = Wall()
                            wall.created_at = datetime.now()
                            wall.room_id = room.id
                            wall.wall_type = val['wall_type'].lower()
                            wall.add_area = val.get('add_area',0)
                            wall.sub_area = val.get('sub_area',0)
                            wall.total_area = val['total_area']
                            wall.save()
                        
                        quotation_items = QuotationItem.objects.filter(quotation_id = quotation.id,process=val['process_id'],product_id=val['product_id'],wall_id=wall.id)
                        
                        if quotation_items.exists():
                            quotation_item = quotation_items[0]
                        else:
                            quotation_item = QuotationItem()
                            quotation_item.created_at = datetime.now()
                            quotation_item.created_by_id = user_id
                            quotation_item.quotation_id = quotation.id
                            
                        quotation_item.wall_id = wall.id
                        quotation_item.price = price_entry.price
                        quotation_item.total_price = (price_entry.price * float(val['total_area'] or 0))
                        quotation_item.process_id = val['process_id']
                        quotation_item.product_id = val['product_id']
                        quotation_item.total_area = val['total_area']
                        quotation_item.wall_type = val['wall_type'].lower()
                        quotation_item.save()
                update_qutation_value(quotation,user_id)
            return Response({'message': self.quotation['created'],'id': quotation.id},status=status.HTTP_200_OK)
        except Exception as e:
            if isinstance(e.args[0],dict):
                return Response(e.args[0],status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'message': e.args[0]},status=status.HTTP_401_UNAUTHORIZED)

class ClubQuotation(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.club_quotation = json_data['club_quotation']
    
    def get(self, request,quotation_id):
        try:
            quotation = Quotation.objects.get(id=quotation_id)
            lead = Lead.objects.filter(id=quotation.lead_id).values('id','name','phone','city_id','alternate_phone','email','status','visit_date_time','channel','channel_reference','project_type','house_type','address').annotate(
                city_name = F('city__city_name')
            ).get()
            lead['quotation_id'] = quotation.id
            rooms = QuotationItem.objects.filter(quotation_id=quotation.id).values('process_id','product_id','wall_type').annotate(
                area = Sum('total_area'),
                totalprice = Sum('total_price'),
            ).distinct()
            return Response({'rooms': rooms, 'lead': lead})
        except Exception as e:
            return Response({'message': self.club_quotation['error_fetching']},status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        try:
            post_data = request.data
            user_id = get_userId_from_access_token(request)
            with transaction.atomic():
                if not post_data['is_updated']:
                    quotation = Quotation.objects.get(id=post_data['quotation_id'])
                else:
                    quotation = create_quotation(post_data, user_id,view_quotation=True)

                for val in post_data['rooms']:
                    quotation_items = QuotationItem.objects.filter(quotation_id=post_data['quotation_id'],process_id=val['process_id'],product_id=val['product_id'],wall_type=val['wall_type'])
                    
                    price_entry = PriceList.objects.filter(process_id=val['process_id'],product_id=val['product_id'],city_id=post_data['city_id'])
                    if price_entry.exists():
                        price_entry = price_entry[0]
                    else:
                        process = Process.objects.get(id=val['process_id'])
                        product = Product.objects.get(id=val['product_id'])
                        raise ValueError({ 'message': self.viewquotation['price_missing'], 'process_id': val['process_id'],'product_id': val['product_id'],'city_id': post_data['city_id'],'process': process.name, 'product': product.name })
                    
                    for row in quotation_items:
                        if not post_data['is_updated']:
                            row.price = price_entry.price
                            row.total_price = (price_entry.price * float(row.total_area))
                            row.process_id = val['process_id']
                            row.product_id = val['product_id']
                            row.save()
                        else:
                            quotation_item = QuotationItem()
                            quotation_item.created_at = datetime.now()
                            quotation_item.created_by_id = user_id
                            quotation_item.quotation_id = quotation.id
                            quotation_item.wall_id = row.wall_id
                            quotation_item.price = price_entry.price
                            quotation_item.total_price = (price_entry.price * float(row.total_area))
                            quotation_item.process_id = val['process_id']
                            quotation_item.product_id = val['product_id']
                            quotation_item.total_area = row.total_area
                            quotation_item.wall_type = row.wall_type
                            quotation_item.save()
                
                update_qutation_value(quotation,user_id)
            return Response({'message': self.club_quotation['created'],'quotation_id': quotation.id},status=status.HTTP_200_OK)
        except Exception as e:
            if isinstance(e.args[0],dict):
                return Response(e.args[0],status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'message': e.args[0]},status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request):
        try:
            delete_data = request.data
            user_id = get_userId_from_access_token(request)
            last_quotation = Quotation.objects.filter(lead_id=delete_data['lead_id']).exclude(id=delete_data['quotation_id']).order_by('-updated_at').first()
            if last_quotation is not None:
                final_quotation = FinalQuotation.objects.get(lead_id=delete_data['lead_id'])
                final_quotation.quotation_id = last_quotation.id
                final_quotation.save()
                update_qutation_value(last_quotation, user_id)
                
            QuotationItem.objects.filter(quotation_id=delete_data['quotation_id']).delete()
            Quotation.objects.filter(id=delete_data['quotation_id']).delete()
            return Response({'message': self.club_quotation['quotation_deleted']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.club_quotation['error_delete']},status=status.HTTP_401_UNAUTHORIZED)

class ViewQuotation(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.view_quotation = json_data['view_quotation']
    
    def get(self, request, lead_id):
        try:
            quotations = Quotation.objects.filter(lead_id=lead_id).values('id','quotation_value','discount','status','accepted_at','created_at').annotate(
                user = Concat(Coalesce(F('created_by__first_name'),Value(''),output_field=CharField()),Value(' '),Coalesce(F('created_by__last_name'),Value(''),output_field=CharField())),
                brand_name = F('brand__brand_name'),
                total_value = Sum('quotationitem__total_price'),
                total_area = Sum('quotationitem__total_area'),
            ).order_by('-updated_at')
            return Response(quotations,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.view_quotation['error']},status=status.HTTP_401_UNAUTHORIZED)

class AcceptQuotation(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        json_data = read_json_file()
        self.accept_quotation = json_data['accept_quotation']
    
    def post(self, request):
        try:
            post_data = request.data
            user_id = get_userId_from_access_token(request)
            if post_data['reset']:
                final_quotation = FinalQuotation.objects.get(lead_id=post_data['lead_id'])
                final_quotation.status = 0
                final_quotation.accepted_at = None
                final_quotation.updated_at = datetime.now()
                final_quotation.updated_by_id = user_id
                final_quotation.save()
                Quotation.objects.filter(lead_id=post_data['lead_id']).update(status = 0,updated_at = datetime.now(),updated_by_id = user_id)
                return Response({'message': self.accept_quotation['reset_message']},status=status.HTTP_200_OK)
            else:
                final_quotation = FinalQuotation.objects.get(lead_id=post_data['lead_id'])
                final_quotation.quotation_id = post_data['quotation_id']
                final_quotation.status = post_data['status']
                final_quotation.accepted_at = datetime.now()
                final_quotation.updated_at = datetime.now()
                final_quotation.updated_by_id = user_id
                final_quotation.save()
                update_qutation_value(final_quotation.quotation, user_id)
            
            return Response({'message': self.accept_quotation['accepted']},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': self.accept_quotation['error']},status=status.HTTP_401_UNAUTHORIZED)