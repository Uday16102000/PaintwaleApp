from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password, check_password

class Service(models.Model):
    service_name = models.CharField(max_length=255, unique=True)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to='services_images/')

    def __str__(self):
        return self.service_name

    class Meta:
        managed = True
        db_table = 'service'


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_detail_images')
    image = models.ImageField(upload_to='services_details_images/')
    finish =models.CharField(max_length=10,default='NA')
    service_detail_title =models.CharField(max_length=255, unique =True,default='NA')


    def __str__(self):
        return f"Image for {self.service.service_name}"

    class Meta:
        managed = True
        db_table = 'service_image'

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
    
def generate_unique_username(name, model_class):
    base_username = slugify(name)[:20]  # Slugify and limit to 20 chars
    username = base_username
    counter = 1
    while model_class.objects.filter(username=username).exists():
        username = f"{base_username}{counter}"
        counter += 1
    return username

class Users(models.Model):
    first_name = models.CharField(max_length=100,blank=True, null=True,default=None)
    last_name = models.CharField(max_length=100,blank=True, null=True,default=None)
    username = models.CharField(max_length=100,blank=False, null=False,unique=True)
    phone = models.CharField(max_length=20,blank=True, null=True,default=None)
    otp = models.IntegerField(blank=True, null=True,default=None)
    email = models.CharField(max_length=50,blank=True, null=True,default=None)
    password = models.CharField(max_length=255,blank=True, null=True,default=None)
    active = models.BooleanField(blank=True, null=True, default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return False
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_active(self):
        return self.active
    
    class Meta:
        managed = True
        db_table = 'users'

@receiver(pre_save, sender=Users)
def set_unique_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = generate_unique_username(instance.first_name,sender)

class ProductBrand(models.Model):
    brand_name = models.CharField(max_length=100,blank=True, null=True,default=None)
    description = models.TextField (blank=True, null=True, default=None)
    image = models.TextField (blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'product_brand'

class ServiceType(models.Model):
    service_name = models.CharField(max_length=255,blank=False, null=False, unique=True)
    service_image = models.TextField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'service_type'
    

class Process(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True, default=None)
    description = models.TextField (blank=True, null=True, default=None)
    image = models.TextField (blank=True, null=True, default=None)
    active = models.BooleanField(blank=True, null=True, default=True)
    servicetype = models.ForeignKey(ServiceType, models.DO_NOTHING,blank=True, null=True, default=None, db_column='servicetype_id')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'process'

class Product(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True, default=None)
    description = models.TextField (blank=True, null=True, default=None)
    product_type = models.CharField(max_length=100, blank=True, null=True, default=None)
    product_category = models.CharField(max_length=100, blank=True, null=True, default=None)
    image = models.TextField (blank=True, null=True, default=None)
    active = models.BooleanField(blank=True, null=True, default=True)
    servicetype = models.ForeignKey(ServiceType, models.DO_NOTHING,blank=True, null=True, default=None, db_column='servicetype_id')
    brand = models.ForeignKey(ProductBrand, models.DO_NOTHING,blank=True, null=True, default=None, db_column='brand_id')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'product'

class Walls(models.Model):
    wall_name = models.CharField(max_length=255,blank=True, null=True, default=None)
    active = models.BooleanField(blank=True, null=True,default=True)
    
    class Meta:
        managed = True
        db_table = 'walls'

class City(models.Model):
    city_name = models.CharField(max_length=100,blank=True, null=True, default=None)
    city_code = models.CharField(max_length=20,blank=True, null=True, default=None)
    active = models.BooleanField(blank=True, null=True, default=True)
    
    class Meta:
        managed = True
        db_table = 'city'

class PriceList(models.Model):
    process = models.ForeignKey(Process, models.DO_NOTHING, db_column='process_id')
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_id')
    city = models.ForeignKey(City, models.DO_NOTHING,db_column='city_id')
    price = models.FloatField(blank=True, null=True, default=None)
    is_lumpsum_rate = models.IntegerField(blank=True, null=True,default=0) # 0: No, 1: Yes
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, models.DO_NOTHING,db_column='created_by',related_name='createdpricelist')
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Users, models.DO_NOTHING,db_column='updated_by',related_name='updatedpricelist')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['process','product','city'],name='unique_process_product_city')
        ]
        managed = True
        db_table = 'price_list'
    
    