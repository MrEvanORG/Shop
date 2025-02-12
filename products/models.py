from django.db import models

# Create your models here.

class products(models.Model):
    pistachio_id = models.AutoField(primary_key=True)
    pistachio_name = models.CharField(max_length=20) #by id
    pistachio_photo = models.ImageField(verbose_name='pstachio-photo',upload_to='prdphotos') #by id
    pistachio_status = models.CharField(max_length=20) #by id
    pistachio_per_ounce = models.IntegerField() #by id
    pistachio_quality = models.CharField(max_length=15) #by id
    pistachio_price = models.FloatField()
    pistachio_gain_status = models.BooleanField(default=False)
    pistachio_gain = models.FloatField()

    def __str__(self):
        return self.pistachio_name

class ordertickets(models.Model): #order a product
    ticket_id = models.AutoField(primary_key=True,verbose_name='شماره تیکت')
    buyer_namelastname = models.CharField(max_length=30,verbose_name='نام خریدار') #need to fill
    buyer_phone = models.CharField(max_length=15,verbose_name='شماره تلفن') #need to fill
    request_title = models.CharField(max_length=20,verbose_name='عنوان درخواست')
    request_discription = models.CharField(max_length=150,verbose_name='متن درخواست')
    ticket_time = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ سفارش')
    ip_address = models.GenericIPAddressField(null=True,blank=True)

    def __str__(self):
        return self.buyer_namelastname

class buytickets(models.Model): #request for buy a non-exist product
    ticket_id = models.AutoField(primary_key=True,verbose_name='شماره تیکت')
    buyer_namelastname = models.CharField(max_length=30,verbose_name='نام خریدار') #need to fill
    buyer_phone = models.CharField(max_length=20,verbose_name='شماره تلفن')
    pistachio = models.ForeignKey(products,on_delete=models.CASCADE,verbose_name='محصول سفارش داده شده')
    gain_product = models.FloatField(verbose_name='مقدار (به کیلو)')
    order_discription = models.CharField(max_length=400,null=True,blank=True,verbose_name='توضیحات سفارش')
    calculated_price = models.FloatField(verbose_name='قیمت نهایی')
    ticket_time = models.DateTimeField(auto_now=True,verbose_name='تاریخ سفارش')
    ip_address = models.GenericIPAddressField(null=True,blank=True)

    def __str__(self):
        return self.buyer_namelastname





# import datetime

# class SaveIpAddressMiddleware(object):
#     """
#         Save the Ip address if does not exist
#     """
#     def process_request(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[-1].strip()
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         try:
#             IpAddress.objects.get(ip_address=ip)
#         except IpAddress.DoesNotExist:             #-----Here My Edit
#               ip_address = IpAddress(ip_address=ip, pub_date=datetime.datetime.now())
#               ip_address.save()
#             return None



