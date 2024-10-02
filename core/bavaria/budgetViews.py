from django.shortcuts import render, redirect, get_object_or_404
from bavaria.models import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F

# Create your views here.

context={
        'acc_succes' : 'Account create successfull',
        'pass_wrong' : 'Password not match',
        'User_login' : 'Login Successfull',
        'save_data' : 'Post Added',
        'update_profile' : 'Update_Profile',
        'pass_update' : 'Password Updated',
    }






# Budget manipulate

@login_required
def budget_planing(request):
    # allBudget=budgetPlaning.objects.all()
    allBudget=budgetPlaning.objects.annotate(total_value=F('marker_cost') + F('cutting_cost') + F('sewing_cost') + F('quality_check') + F('ironing') + F('packing_cost'))


    return render(request, 'budget/budgetPlaning.html', {'budgetList': allBudget})



@login_required
def budgetForm(request):
    # allcategory=categoryModel.objects.all()

    # getCategoryID = request.GET.get('catid', None)

    # sub_category=sub_categoryModel.objects.filter(category=getCategoryID)

    # get_sub_CategoryID = request.GET.get('subcatid', None)

    # allOrder=Order.objects.filter(sub_category=get_sub_CategoryID)
    # print('all order', allOrder)


    allcategory=categoryModel.objects.all()

    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)

    state = None
    district = None
	
    if countryid:
	
        getcountry = categoryModel.objects.get(id=countryid)
        print('cat-id' , getcountry)
        state = sub_categoryModel.objects.filter(category=getcountry)
        print('cat-obj', state)
		
    if stateid:
	
        getstate = sub_categoryModel.objects.get(id=stateid)
        print('sub-cat-id' , getcountry)
        district = Order.objects.filter(sub_category=getstate)
        print('sub-cat-obj', state)


    context = {
            'allcat' : allcategory,
            'all_sub_cat' : state,
            'all_ref' : district,
        }

    

    if request.method=="POST":
        bDate=request.POST.get('bDate')
        catid=request.POST.get('cat')
        cat = get_object_or_404(categoryModel, id=catid)
        subcatid=request.POST.get('subCat')
        subcat = get_object_or_404(sub_categoryModel, id=subcatid)
        orderRef=request.POST.get('orRef')
        orRef = get_object_or_404(Order, id=orderRef)
        name=request.POST.get('name')
        mkCost=request.POST.get('mkCost')
        cuttingCost=request.POST.get('cuttingCost')
        sewCost=request.POST.get('sewCost')
        qc=request.POST.get('qc')
        ironing=request.POST.get('ironing')
        pkgCost=request.POST.get('pkgCost')
        budgetCost=request.POST.get('budgetCost')
        actCost=request.POST.get('actCost')
        qty=request.POST.get('qty')


        save_budget = budgetPlaning(
            date=bDate,
            category=cat,
            sub_category=subcat,
            order_reference=orRef,
            name=name,
            marker_cost=mkCost,
            cutting_cost=cuttingCost,
            sewing_cost=sewCost,
            quality_check=qc,
            ironing=ironing,
            packing_cost=pkgCost,
            budget_cost=budgetCost,
            actual_cost=actCost,
            qty=qty,
        )
        save_budget.save()
        return redirect('budget_planing')




    # allcategory = categoryModel.objects.all()

    # countryid = request.GET.get('country', None)
    # stateid = request.GET.get('state', None)

    # state = None
    # district = None

    # if countryid:
    #     getcountry = categoryModel.objects.get(id=countryid)
    #     state = sub_categoryModel.objects.filter(category=getcountry)

    # if stateid:
    #     getstate = sub_categoryModel.objects.get(id=stateid)
    #     district = Order.objects.filter(sub_category=getstate)

    # context = {
    #     'allcat': allcategory,
    #     'all_sub_cat': state or [],  # Use empty list if state is None
    #     'all_ref': district or [],    # Use empty list if district is None
    # }

    # if request.method == "POST":
    #     bDate = request.POST.get('bDate')
    #     catid = request.POST.get('cat')  # Use 'cat' for category
    #     print('catid',catid)
    #     subcatid = request.POST.get('subCat')  # Use 'subCat' for subcategory
    #     orderRef = request.POST.get('orRef')

    #     # Validate that category and subcategory are selected
    #     # if not catid or not subcatid or not orderRef:
    #     #     # Handle the error (e.g., return error message to the user)
    #     #     context['error'] = "Please select all required fields."
    #     #     return render(request, 'budgetForm.html', context)

    #     cat = get_object_or_404(categoryModel, id=catid)
    #     subcat = get_object_or_404(sub_categoryModel, id=subcatid)
    #     orRef = get_object_or_404(Order, id=orderRef)

    #     # Capture all other form data
    #     name = request.POST.get('name')
    #     mkCost = request.POST.get('mkCost')
    #     cuttingCost = request.POST.get('cuttingCost')
    #     sewCost = request.POST.get('sewCost')
    #     qc = request.POST.get('qc')
    #     ironing = request.POST.get('ironing')
    #     pkgCost = request.POST.get('pkgCost')
    #     budgetCost = request.POST.get('budgetCost')
    #     actCost = request.POST.get('actCost')
    #     qty = request.POST.get('qty')

    #     # Save the budget plan
    #     save_budget = budgetPlaning(
    #         date=bDate,
    #         category=cat,
    #         sub_category=subcat,
    #         order_reference=orRef,
    #         name=name,
    #         marker_cost=mkCost,
    #         cutting_cost=cuttingCost,
    #         sewing_cost=sewCost,
    #         quality_check=qc,
    #         ironing=ironing,
    #         packing_cost=pkgCost,
    #         budget_cost=budgetCost,
    #         actual_cost=actCost,
    #         qty=qty,
    #     )
    #     save_budget.save()
    #     # Optionally redirect or render a success message
    #     return redirect('budget_planing')  # Replace with your success view name

    
    return render(request, 'budget/budgetForm.html', context)


def budgetStart(request, myid):
    budgetstID = get_object_or_404(budgetPlaning, id=myid)
    budgetstID.status="Start"
    budgetstID.save()
    return redirect('budget_planing')  

def onGoing(request, myid):
    budgetstID = get_object_or_404(budgetPlaning, id=myid)
    budgetstID.status="On_Going"
    budgetstID.save()
    return redirect('budget_planing')  

def budgetEnd(request, myid):
    budgetstID = get_object_or_404(budgetPlaning, id=myid)
    budgetstID.status="End"
    budgetstID.save()
    return redirect('budget_planing')  



def ab(request):
    
    if request.method=="POST":
        catid=request.POST.get('cat')
        print('aaaaaaa', catid)
        cat = get_object_or_404(categoryModel, id=catid)
        print(cat)
        subcatid=request.POST.get('subcat')
        print('bbbbbb', subcatid)
        
        subcat = get_object_or_404(sub_categoryModel, id=subcatid)
        print(subcatid)
        orderRef=request.POST.get('order')
        orRef = get_object_or_404(Order, id=orderRef)

        bDate=request.POST.get('bDate')
        name=request.POST.get('name')
        mkCost=request.POST.get('mkCost')
        cuttingCost=request.POST.get('cuttingCost')
        sewCost=request.POST.get('sewCost')
        qc=request.POST.get('qc')
        ironing=request.POST.get('ironing')
        pkgCost=request.POST.get('pkgCost')

        actCost=request.POST.get('actCost')
        qty=request.POST.get('qty')


        save_budget = budgetPlaning(
            date=bDate,
            category=cat,
            sub_category=subcat,
            order_reference=orRef,
            name=name,
            marker_cost=mkCost,
            cutting_cost=cuttingCost,
            sewing_cost=sewCost,
            quality_check=qc,
            ironing=ironing,
            packing_cost=pkgCost,
            actual_cost=actCost,
            qty=qty,
        )
        save_budget.save()
        if orRef.budget_plan == 'Pending':
            orRef.budget_plan = 'Created'
            orRef.save()
        return redirect('budget_planing')
    return render(request, 'budget/ab.html')


def getBudget(request, bID):
    # fetcgData = get_object_or_404(budgetPlaning, order_reference =bID)
    fetcgData=budgetPlaning.objects.filter(order_reference=bID).annotate(total_value=F('marker_cost') + F('cutting_cost') + F('sewing_cost') + F('quality_check') + F('ironing') + F('packing_cost'))
    return render(request, 'budget/budgetView.html', {'fetch':fetcgData})