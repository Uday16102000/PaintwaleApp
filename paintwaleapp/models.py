from django.db import models

# Create your models here.


from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#     name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     first_name = models.CharField(max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     action_time = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'

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