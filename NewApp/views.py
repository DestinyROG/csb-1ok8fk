from django.shortcuts import render,redirect
from NewApp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

def home(request):
    banner=Banner_image.objects.all()
    context={
        'banner':banner,
    }
    return render(request,'Store\Layout\home.html',context=context)

def Collections(request):
    ourCollections=Category.objects.all()
    context={
        'ourCollections':ourCollections,
    }
    return render(request, 'Store\Layout\collections.html',context)

def Collectionsview(request,name):
    if Category.objects.filter(urlname=name):
        category=Category.objects.all().get(urlname=name)
        products=Product.objects.all().filter(category=name)
        print(type(category))
        context={
            "products":products,
            'category':category,
        }
        # print(Product.objects.filter(category=name))
    return render(request,'Store\Layout\Product\product.html',context)


def Productview(request,cate,prod):
    if Product.objects.filter(category=cate,name=prod) and Category.objects.filter(urlname=cate):
        categoryname=Category.objects.get(urlname=cate)
        itemname=Product.objects.get(category=cate,name=prod)
        context={
            'itemname':itemname,
            'categoryname':categoryname,
        }
        return render(request,'Store\Layout\Product\productview.html', context)


def Accessdenied(request):
    return render(request,'Store/accessdenied.html')


@login_required(login_url='accessdenied')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Add_to_cart(request,cate,name,qty):
    prod=Product.objects.all().get(category=cate,name=name)
    cart=Cart.objects.all().filter(user=request.user)
    check=0
    if len(cart)==0:
        add=Cart(category=prod.category,name=prod.name,product_image=prod.product_image,price=prod.selling_price,quantity=qty,user=request.user)
        add.save()
    else:
        for i in cart:
            if i.name==prod.name and i.category==prod.category:
                check+=1
            else:
                check+=0
        if check==1:
            for i in cart:
                if i.name==prod.name and i.category==prod.category:
                    i.quantity+=qty
                    i.save()
        else:
            add=Cart(category=prod.category,name=prod.name,product_image=prod.product_image,price=prod.selling_price,quantity=qty,user=request.user)
            add.save()
        
    return redirect(f"/collections/{cate}")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Cartview(request):
    cart=Cart.objects.all()
    context={
        'cart':cart,
    }
    return render(request,'Store\Layout\cart.html',context=context)