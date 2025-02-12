from django import forms
# from .models import
# from .models import tickets

class OrderForm(forms.Form):
    buyer_namelastname = forms.CharField(max_length=30,required=True,label='نام و نام خانوادگی')
    buyer_phonenumber = forms.CharField(max_length=15,required=True,label='شماره تلفن')
    request_title = forms.CharField(max_length=20,required=True,label='عنوان') #need to fill
    request_text = forms.CharField(max_length=200,required=True,label='متن درخواست') #need to fill

    def clean_buyer_namelastname(self):
        name = self.cleaned_data['buyer_namelastname']
        if len(name) >= 29:
            raise forms.ValidationError('بیش از حد مجاز است')
        elif len(name) < 5 :
            raise forms.ValidationError('بسیار کوتاه است')
        return name
    
    def clean_buyer_phonenumber(self):
        phone = self.cleaned_data['buyer_phonenumber']
        if len(str(phone)) < 10 :
            raise forms.ValidationError('بسیار کوتاه است')
        return phone
        
    def clean_request_title(self):
        title = self.cleaned_data['request_title']
        print(len(title))
        if len(title) > 19 :
            print('# ERROR RAISED')
            raise forms.ValidationError('بیش از حد مجاز است')
        elif len(title) < 5 :
            raise forms.ValidationError('بسیار کوتاه است')
        return title
        
    def clean_request_text(self):
        text = self.cleaned_data['request_text']
        if len(text) >= 198 :
            raise forms.ValidationError('بیش از حد مجاز است')
        elif len(text) < 5 :
            raise forms.ValidationError('بسیار کوتاه است')
        return text
        


class BuyForm(forms.Form):
    buyer_namelastname = forms.CharField(max_length=30,required=True,label='نام و نام خانوادگی') #need to fill
    buyer_phone = forms.CharField(max_length=15,required=True,label='شماره تلفن')
    gain_product = forms.FloatField(required=True,label='مقدار (به کیلو)')
    order_discription = forms.CharField(required=False,max_length=400,label='توضیحات سفارش')

    def clean_buyer_namelastname(self):
        name = self.cleaned_data['buyer_namelastname']
        if len(name) >= 29:
            raise forms.ValidationError('بیش از حد مجاز است')
        elif len(name) < 5 :
            raise forms.ValidationError('بسیار کوتاه است')
        return name
    
    def clean_buyer_phone(self):
        phone = self.cleaned_data['buyer_phone']
        if len(str(phone)) < 10 :
            raise forms.ValidationError('بسیار کوتاه است')
        return phone

    def clean_gain_product(self):
        gain = self.cleaned_data['gain_product']
        if float(gain) < 0.5 :
            raise forms.ValidationError('نمیتواند کمتر از 500 گرم باشد')
        elif float(gain) > 10 :
            raise forms.ValidationError('در حال حاضر امکان ثبت سفارش بیش از 10 کیلوگرم وجود ندارد')
        
        return gain

    def clean_order_discription(self):
        text = self.cleaned_data['order_discription']
        if len(text) >= 390 :
            raise forms.ValidationError('بیش از حد مجاز است')

        return text
    


# product_id = models.ForeignKey(products,on_delete=models.PROTECT)
# gain_of_pistachio = models.IntegerField() #need ti fill
# buyer_phone = models.CharField(max_length=20) #need to fill
# buyer_ip = models.GenericIPAddressField()
# ticket_time = models.DateTimeField(auto_now_add=True)


# buy product : 
# name -lastname 
#buyer phonenumber
#gain of product 
#prcice calcualted
# request text


# order product : 
#name -lastname
#buyer phonenumber
#request title
# request text



