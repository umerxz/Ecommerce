from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.http import JsonResponse
import json
# Create your views here.
def vendorHome(request):
    return render(request,'userapp/vendorhome.html')
def vendorProdList(request):
    current_user=request.user
    my_user=models.MyUser.objects.get(user=current_user.id)
    prod=models.Product.objects.filter(seller=my_user)
    return render(request,'userapp/vendorprodlist.html',{'prodt':prod})
def vendorProdAdd(request):
    form=forms.AddProductForm()
    if request.method=='POST':
        form=forms.AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            current_user=request.user
            my_user=models.MyUser.objects.get(user=current_user.id)
            prod=form.save(commit=False)
            prod.seller=my_user
            prod.save()
            return redirect('userss:vendor-prod-list-url')
    else:
        form=forms.AddProductForm()
    return render(request,'userapp/vendorprodadd.html',{'form':form})
def vendorProdUpdate(request,id):
    prod=get_object_or_404(models.Product,id=id)
    if request.method=='POST':
        form=forms.AddProductForm(request.POST,instance=prod)
        if form.is_valid():
            current_user=request.user
            my_user=models.MyUser.objects.get(user=current_user.id)
            prod=form.save(commit=False)
            prod.seller=my_user
            prod.save()
            return redirect('userss:vendor-prod-list-url')
    else:
        form=forms.AddProductForm(instance=prod)
    return render(request,'userapp/vendorprodupdate.html',{'form':form})
def vendorProdDelete(request,id):
    prod=get_object_or_404(models.Product,id=id)
    if request.method=='POST':
        prod.delete()
        return redirect('userss:vendor-prod-list-url')
    return render(request,'userapp/vendorproddelete.html',{'prod':prod})
def vendorOrders(request):
    current_user=request.user.myuser
    prod=models.Product.objects.filter(seller=current_user)
    order=models.Order.objects.all()
    item=models.Item.objects.filter(product__in=prod)

    print(prod)
    print(order)
    print(item)
    print()

    return render(request,'userapp/vendororders.html',{'order':order,'item':item})
def vendorOrdersByCustomer(request):

    return render(request,'userapp/ordersbycustomer.html',{})
def basePage(request):
    return render(request,'base.html')
def Signup(request):
    form1=forms.CustomerForm1()
    form2=forms.CustomerForm2()
    if request.method=='POST':
        form1=forms.CustomerForm1(request.POST)
        form2=forms.CustomerForm2(request.POST)
        if form1.is_valid() and form2.is_valid():
            user1=form1.save()
            user2=form2.save(commit=False)
            user2.user=user1
            user2.save()
            messages.success(request,'Account Created!')
            return redirect('userss:login-url')
    else:
        form1=forms.CustomerForm1()
        form2=forms.CustomerForm2()
    context={'form1':form1,'form2':form2}
    return render(request,'userapp/signup.html',context)
def log_in(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            my_user=models.MyUser.objects.get(user_id=user.id)
            if my_user.Register_As=='S':
                return redirect('userss:vendor-home-url')
            elif my_user.Register_As=='B':
                return redirect('userss:customer-prod-list-url')
    else:
        form=AuthenticationForm()
    return render(request,'userapp/login.html',{'form':form})
def log_out(request):
    logout(request)
    return redirect('userss:login-url')

def customerProdList(request):
    prod=models.Product.objects.all()
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def jacketsPage(request):
    prod=models.Product.objects.filter(type='Jackets')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def shirtsPage(request):
    prod=models.Product.objects.filter(type='Shirts')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def tshirtsPage(request):
    prod=models.Product.objects.filter(type='T-shirts')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def jeansPage(request):
    prod=models.Product.objects.filter(type='Jeans')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def shortsPage(request):
    prod=models.Product.objects.filter(type='Shorts')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def tightsPage(request):
    prod=models.Product.objects.filter(type='Tights')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def trousersPage(request):
    prod=models.Product.objects.filter(type='Trousers')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def joggersPage(request):
    prod=models.Product.objects.filter(type='Joggers')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def sneakersPage(request):
    prod=models.Product.objects.filter(type='Sneakers')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def pumpsPage(request):
    prod=models.Product.objects.filter(type='Pumps')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})
def heelsPage(request):
    prod=models.Product.objects.filter(type='Heels')
    return render(request,'userapp/customerprodlist.html',{'prod':prod})

def womenPage(request):
    prod=models.Product.objects.filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenJacketsPage(request):
    prod=models.Product.objects.filter(type='Jackets').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenShirtsPage(request):
    prod=models.Product.objects.filter(type='Shirts').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenTshirtsPage(request):
    prod=models.Product.objects.filter(type='T-shirts').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenJeansPage(request):
    prod=models.Product.objects.filter(type='Jeans').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenShortsPage(request):
    prod=models.Product.objects.filter(type='Shorts').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenTightsPage(request):
    prod=models.Product.objects.filter(type='Tights').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenTrousersPage(request):
    prod=models.Product.objects.filter(type='Trousers').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenJoggersPage(request):
    prod=models.Product.objects.filter(type='Joggers').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenSneakersPage(request):
    prod=models.Product.objects.filter(type='Sneakers').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenPumpsPage(request):
    prod=models.Product.objects.filter(type='Pumps').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})
def womenHeelsPage(request):
    prod=models.Product.objects.filter(type='Heels').filter(category='W')
    return render(request,'userapp/womenlist.html',{'prod':prod})

def menPage(request):
    prod=models.Product.objects.filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menJacketsPage(request):
    prod=models.Product.objects.filter(type='Jackets').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menShirtsPage(request):
    prod=models.Product.objects.filter(type='Shirts').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menTshirtsPage(request):
    prod=models.Product.objects.filter(type='T-shirts').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menJeansPage(request):
    prod=models.Product.objects.filter(type='Jeans').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menShortsPage(request):
    prod=models.Product.objects.filter(type='Shorts').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menTightsPage(request):
    prod=models.Product.objects.filter(type='Tights').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menTrousersPage(request):
    prod=models.Product.objects.filter(type='Trousers').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menJoggersPage(request):
    prod=models.Product.objects.filter(type='Joggers').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menSneakersPage(request):
    prod=models.Product.objects.filter(type='Sneakers').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menPumpsPage(request):
    prod=models.Product.objects.filter(type='Pumps').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})
def menHeelsPage(request):
    prod=models.Product.objects.filter(type='Heels').filter(category='M')
    return render(request,'userapp/menlist.html',{'prod':prod})

def kidsPage(request):
    prod=models.Product.objects.filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsJacketsPage(request):
    prod=models.Product.objects.filter(type='Jackets').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsShirtsPage(request):
    prod=models.Product.objects.filter(type='Shirts').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsTshirtsPage(request):
    prod=models.Product.objects.filter(type='T-shirts').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsJeansPage(request):
    prod=models.Product.objects.filter(type='Jeans').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsShortsPage(request):
    prod=models.Product.objects.filter(type='Shorts').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsTightsPage(request):
    prod=models.Product.objects.filter(type='Tights').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsTrousersPage(request):
    prod=models.Product.objects.filter(type='Trousers').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsJoggersPage(request):
    prod=models.Product.objects.filter(type='Joggers').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsSneakersPage(request):
    prod=models.Product.objects.filter(type='Sneakers').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsPumpsPage(request):
    prod=models.Product.objects.filter(type='Pumps').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})
def kidsHeelsPage(request):
    prod=models.Product.objects.filter(type='Heels').filter(category='K')
    return render(request,'userapp/kidslist.html',{'prod':prod})

def cartView(request):
    current_user=request.user.myuser
    order,created=models.Order.objects.get_or_create(customer=current_user,is_complete=False)
    items=order.item_set.all()
    return render(request,'userapp/cart.html',{'items':items,'order':order})

def checkoutView(request):
    current_user=request.user.myuser
    order,created=models.Order.objects.get_or_create(customer=current_user,is_complete=False)
    items=order.item_set.all()
    return render(request,'userapp/checkout.html',{'items':items,'order':order})

def payView(request):
    current_user=request.user.myuser
    order,created=models.Order.objects.get_or_create(customer=current_user,is_complete=False)
    order.is_complete=True
    order.save()
    return redirect('userss:customer-prod-list-url')

def updateOrderView(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    current_user=request.user.myuser
    product=models.Product.objects.get(id=productId)
    order,created=models.Order.objects.get_or_create(customer=current_user,is_complete=False)
    item,created=models.Item.objects.get_or_create(product=product,order=order)
    if action=='add':
        item.quantity+=1
        product.stock-=1
    elif action=='remove':
        item.quantity-=1
        product.stock+=1
    item.save()
    product.save()
    if item.quantity<=0:
        item.delete()
    return JsonResponse('ADDED',safe=False)
