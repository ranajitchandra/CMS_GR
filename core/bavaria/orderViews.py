from django.shortcuts import render, redirect, get_object_or_404
from bavaria.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Max

# Create your views here.

context={
        'acc_succes' : 'Account create successfull',
        'pass_wrong' : 'Password not match',
        'User_login' : 'Login Successfull',
        'save_data' : 'Post Added',
        'update_profile' : 'Update_Profile',
        'pass_update' : 'Password Updated',
    }


# Order manipulate
@login_required
def orderForm(request):
    allcategory=categoryModel.objects.all()

    getCategoryID = request.GET.get('catid', None)
    sub_category=sub_categoryModel.objects.filter(category=getCategoryID)

    getsubCategoryID = request.GET.get('subcatid', None)
    brand=brandNmaeModel.objects.filter(category=getsubCategoryID)
    
    if Order.objects.count() == 0:
        autoNum = 'bge1'  # Starting value for autoNum
    else:
        max_order_reference = Order.objects.aggregate(max=Max('order_reference'))['max']
        if max_order_reference:
            # Extract the numeric part
            numeric_part_str = max_order_reference[3:]  # Adjust according to your format
            
            if numeric_part_str.isdigit():  # Check if the remaining string is numeric
                numeric_part = int(numeric_part_str)
                autoNum = f'bge{numeric_part + 1}'  # Create new reference
            else:
                autoNum = 'bge1'  # Fallback if the format is unexpected
        else:
            autoNum = 'bge1'  # Fallback if max_order_reference is NoneoNum = 'bge1'  # Fallback

    context = {
            'allcat' : allcategory,
            'all_sub_cat' : sub_category,
            'all_brand' : brand,
            'autonum' : autoNum,
        }
    
    if request.method=="POST":
        catid=request.POST.get('cat')
        cat = get_object_or_404(categoryModel, id=catid)
        subcatid=request.POST.get('subCat')
        subcat = get_object_or_404(sub_categoryModel, id=subcatid)
        brandid=request.POST.get('brandName')
        brand = get_object_or_404(brandNmaeModel, id=brandid)
        ref=request.POST.get('orderNum')
        name=request.POST.get('name')
        orDate=request.POST.get('orDate')
        deDate=request.POST.get('deDate')
        qnt=request.POST.get('qnt')


        save_order = Order(
            category=cat,
            sub_category=subcat,
            brandModel=brand,
            order_reference=ref,
            order_date=orDate,
            delivery_date=deDate,
            name=name,
            quantity=qnt,
        )
        save_order.save()
        return redirect('orderSummery')

    return render(request, "orders/orderForm.html", context)




@login_required
def orderSummery(request):
    allOrdelList=Order.objects.all()

    return render(request, "orders/orderSummery.html", {'allOrder': allOrdelList})


def orderDelete(request, orderid):
    get_order = Order.objects.get(id = orderid)
    get_order.delete()
    return redirect('orderSummery')


@login_required
def orderEdit(request, orderid):
    get_order = Order.objects.get(id = orderid)
    
    return render(request, 'orders/orderEdit.html', {'target_order': get_order})


def orderUpdate(request):
    
    if request.method == "POST":
        id = request.POST.get('id', None)
        target_order = Order.objects.get(id=id)

        or_date = request.POST.get('OrDate', None)
        de_date = request.POST.get('DeDate', None)
        name = request.POST.get('name', None)
        qnt = request.POST.get('qnt')

        target_order.order_date=or_date
        target_order.delivery_date=de_date
        target_order.name=name
        target_order.quantity=qnt
        target_order.save()
        messages.success(request, "Order updated successfully!")

        return redirect('orderSummery')
    