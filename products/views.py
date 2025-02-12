from django.shortcuts import render ,get_object_or_404 , redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import products , ordertickets ,buytickets
from .forms import OrderForm , BuyForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

# Create your views here.
#salehih1227@gmail.com
def Generate_email(type,name,phone,title,discription,pistachio,gain,price):
    if type == 'order':
        text = f"""نام درخواست دهنده : {name}
شماره تماس : {phone}
عنوان درخواست : {title}
شرح درخواست : {discription}
محصول سفارش داده شده : {pistachio}
"""
        send_mail('درخواست خرید جدید',text,'pestina.ir@gmail.com',['ehsan66845@gmail.com'],fail_silently=True)
    if type == 'buy':
        text = f"""نام خریدار : {name}
شماره تماس : {phone}
توضیحات : {discription}
مقدار سفارش داده شده : {gain} کیلوگرم
هزینه نهایی : {price} تومان """
        send_mail('سفارش خرید جدید',text,'pestina.ir@gmail.com',['ehsan66845@gmail.com'],fail_silently=True)

def get_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def calculate_price(gain_product,price_product):
    price = int(gain_product) * int(price_product)
    string = f'هزینه ارسال رایگان +  {price} تومان  هزینه محصول  > جمع : {price}'
    return string , price

def homepage(request):
    template = loader.get_template('nindex.html')
    return HttpResponse(template.render())

def view_products(request):
    template = loader.get_template('nproducts.html')
    prd = products.objects.all()
    pagin = Paginator(prd,2)
    page_number = request.GET.get('page')
    page_obj = pagin.get_page(page_number)
    context = {'products': page_obj}
    return HttpResponse(template.render(context))

@csrf_protect
def order_product(request):
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        ticket = ordertickets.objects.create()
            # ticket.save()
        if not form.errors and form.is_valid():
            ticket.buyer_namelastname = form.cleaned_data['buyer_namelastname']
            ticket.buyer_phone = form.cleaned_data['buyer_phonenumber']
            ticket.request_title = form.cleaned_data['request_title']
            ticket.request_discription = form.cleaned_data['request_text']
            ticket.ip_address = get_ip(request)
            ticket.save()
            Generate_email('order',
                           ticket.buyer_namelastname,
                           ticket.buyer_phone,ticket.request_title,
                           ticket.request_discription,0,0,0,
                           )
            context = {"buyer_name":form.cleaned_data['buyer_namelastname'],
                       "buyer_phone":form.cleaned_data['buyer_phonenumber']}
            return render(request,"registered.html",context)
        else:
            ticket.delete()
            context = {'form':form}
            return render(request,"order_product.html",context)

    if request.method == 'GET':
            context = None
            return render(request,"order_product.html",context)

def buy_product(request,pid):
    order_data = request.session.get("order_data")
    if order_data:
        del request.session["order_data"]
    

    prd = products.objects.get(pistachio_id=pid)
    if request.method == 'POST':
        form = BuyForm(data=request.POST)
        if not form.errors and form.is_valid():

            form_data = form.cleaned_data
            price_string , price = calculate_price(form.cleaned_data['gain_product'],prd.pistachio_price)

            request.session["order_data"] = {
                "prd":pid,
                "form_data":form_data,
                "price":price,
            }
            context = {'form':form,'prd':prd,'price':price_string}
            return render(request,'calculate.html',context)
        else:
            context = {'form':form,'product':prd} #return prodct and form error and form content
            return render(request,"buy_product.html",context)
            
    elif request.method == 'GET':
        context = {'product':prd}
        return render(request, "buy_product.html", context)
    
def confirm_buy(request):
    order_data = request.session.get("order_data")
    if not order_data:
        return HttpResponse('sorry something happend in backend process and your order does not save\nThis is an Error !')
    else:
        del request.session["order_data"]


    form = BuyForm(data=order_data['form_data'])
    pid = order_data['prd']
    price = order_data['price']

    print(form,pid,price)
    prd = products.objects.get(pistachio_id=pid)

    ticket = buytickets.objects.create(
    buyer_namelastname = form.cleaned_data['buyer_namelastname'],
    buyer_phone = form.cleaned_data['buyer_phone'],
    pistachio = prd,
    gain_product = form.cleaned_data['gain_product'],
    order_discription = form.cleaned_data['order_discription'],
    calculated_price = price,
    ip_address = get_ip(request))
    ticket.save()
    Generate_email('buy',form.cleaned_data['buyer_namelastname'],form.cleaned_data['buyer_phone'],0,form.cleaned_data['order_discription'],prd.pistachio_name,form.cleaned_data['gain_product'],price)
# Generate_email(type,name,phone,title,discription,pistachio,gain,price)
    context = {'buyer_name':ticket.buyer_namelastname,'buyer_phone':ticket.buyer_phone}
    return render(request,'registered.html',context)
    

def about_us(request):
    return render(request,"nabout_us.html")

def farmer_register(request):
    return HttpResponse('this page is not ready yet !')


