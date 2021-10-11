from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from .models import List,Product
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages
# Create your views here.
def home(request):
    _list = List.objects.all()
    _product = Product.objects.all()
    
    _list = {
        'list': _list,
        'product': _product
    }
    
    return render(request,"Home/Home.html",{'list': _list})
def category(request,id):
        _product = Product.objects.filter(listid=id)
        list = List.objects.all()
        _list = {
        'list': list,
        'product': _product
    }
       
    # return HttpResponse({'category': _category})
        # _category_json = json.dumps(_category)
        print(_list)
        return render(request,"Home/Home.html",{'list': _list})


@login_required
def productsinfo(request,id):
        _list = List.objects.all()
        _product = Product.objects.all()
    # if request.user.is_authenticated:
        
        _sp = Product.objects.get(id=id)
        _list = {
            'list': _list,
            'product': _product,
            'sanpham': _sp
        }
        
        return render(request,"Home/productsinfo.html",{'list':_list})
def loginr(request):
    return render(request,"Home/Login.html")
def sigup(request):
    return render(request,"Home/Sigup.html")


def rlogin(request):
    _username = request.POST['name']
    _password = request.POST['password']
    user = authenticate(username=_username, password=_password)
    if user is not None:
        login(request, user)
        request.session['user'] = _username
        
        if request.POST.get('next'):
            return redirect(request.POST.get('next'))
        else:
            return redirect('home')
            return redirect(request.GET.get('next'))
        
    else:
        messages.info(request, 'Sai tài khoản hoặc mật khẩu đã nhập')
        return redirect('login')
  
        
   
def rsigup(request):
    _name = request.POST['name']
    _email = request.POST['email']
    _password = request.POST['password1']
    try:
        us = User.objects.get(username=_name)
        messages.info(request, 'Kiểm tra lại thông tin đã nhập')
        return redirect('sigup')
    except:
        _user = User.objects.create_user(_name,_email,_password)
        _user.save()
        return redirect('login')

def logout_view(request):
    logout(request)
    _list = List.objects.all()
    _product = Product.objects.all()
    _list = {
        'list': _list,
        'product': _product
    }
    return render(request,"Home/Home.html",{'list': _list})
    


def cart(request):
    _total = 0
    
    try:
        cart = request.session['cart']
        for key,value in cart.items():
            _total += int(value['price'])*int(value['num'])
    except:
        _total = 0
    return render(request,"Home/Cart.html",{'total':_total})
    # return render(request,"Home/Cart.html")
_cart ={}

def addcart(request):

    if int(request.POST.get('id')) == 987431:
        
        request.session['cart'] = {}
        global _cart
        _cart = {}
    elif request.is_ajax():
            id = request.POST.get('id')
            sp = Product.objects.get(id=id)
            name = sp.name
            price = sp.price
            promotion = sp.promotion
            num = request.POST.get('num')
            statuss = False
            for i, element in _cart.items():
            
                try:
                    
                    if element['name'] == name:
                        x = element['num']
                    
                        _cart[i]['num'] =  int(num) + int(x)
                    
                        statuss = True     
                
                except:
                    print('opss except')
                    
                    
            if statuss == False:
                x = len(_cart)
                _cart[x+1]={'name': name, 'num' : num, 'price' : price, 'promotion' : promotion}
            print('###cart')
            print(_cart)    
            request.session['cart'] = _cart
            cartinfo = request.session['cart']
        # html = request.render_to_string("trangchu/giohang.html",cartinfo)
        
    else:
        message = "opss Not ajax"
    # return HttpResponse(json.dumps( cartinfo ))
    return HttpResponse('run')
