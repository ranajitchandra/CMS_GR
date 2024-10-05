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
def base(request):
    return render(request, "base.html")


def signupPage(request):

    if request.method=='POST':
        
        
        user_name=request.POST.get('user_name')
        email=request.POST.get('email')
        
        password=request.POST.get('pass')
        confirm_password=request.POST.get('cpass')
        
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        user_role=request.POST.get('user_role')
        img=request.FILES.get('img')
        

        if password==confirm_password:
            user=Custom_User.objects.create_user(
                username=user_name,
                password=confirm_password,
                email=email,
                )
            user.dob=dob
            user.gender=gender
            user.user_role=user_role
            user.image=img
            user.save()
            messages.success(request, context['acc_succes'])
            return redirect('signin')
        else:
            messages.warning(request, context['pass_wrong'])
    
    return render(request, 'register.html')

def signin(request):

    if request.method=='POST':
        user_email=request.POST.get('email')
        pass_word=request.POST.get('pass')
        print('p', user_email)
        print('ppp', pass_word)
        user_login=authenticate(username=user_email, password=pass_word)
        print(user_login)
        if user_login:
            login(request, user_login)
            return redirect('home')
        
    return render(request, "login.html")

def logoutpage(request):
    logout(request)
    return redirect('signin')




def home(request):
    return render(request, "index.html")

def retailerReg(request):
    
    return render(request, "reg_retailer.html")


def reg_unitReg(request):
    
    return render(request, "reg_unitReg.html")

def reg_ProductionSale(request):
    
    return render(request, "reg_ProductionSale.html")

def reg_wholeSale(request):
    
    return render(request, "reg_wholeSale.html")




# Category manipulate
@login_required
def categoryPage(request):
    allcategory=categoryModel.objects.all()
    all_sub_category=sub_categoryModel.objects.all()
    brandNma=brandNmaeModel.objects.all()
    context = {
            'allcat' : allcategory,
            'all_sub_cat' : all_sub_category,
            'all_brand' : brandNma,
        }
    return render(request, "category.html", context)


@login_required
def categoryForm(request):

    if request.method=='POST':
        category_name=request.POST.get('catName')
        
        save_category = categoryModel(
            name = category_name,
        )
        save_category.save()
        return redirect('categoryPage')

    return render(request, "categoryForm.html")



def brandNameForm(request):

    allcategory=categoryModel.objects.all()

    categoryid = request.GET.get('category', None)
    subCategoryid = request.GET.get('subCategory', None)

    state = None
    district = None
	
    if categoryid:
	
        getcountry = categoryModel.objects.get(id=categoryid)
        
        state = sub_categoryModel.objects.filter(category=getcountry)

    if subCategoryid:
	
        getsubCategory = sub_categoryModel.objects.get(id=subCategoryid)
        
        district = Order.objects.filter(sub_category=getsubCategory)
        
    context = {
            'allcat' : allcategory,
            'all_sub_cat' : state,
            'all_ref' : district,
        }


    if request.method=="POST":
        
        catid=request.POST.get('cat')
        cat = get_object_or_404(categoryModel, id=catid)
        subcatid=request.POST.get('subCat')
        subcat = get_object_or_404(sub_categoryModel, id=subcatid)
        
        brandName=request.POST.get('brandName')
        


        save_budget = brandNmaeModel(
            category=cat,
            subcategory=subcat,
            name=brandName,
        )
        save_budget.save()
        return redirect('categoryPage')

    return render(request, "brandMenuForm.html", context)


@login_required
def categoryDelete(request, catid):
    get_cat = categoryModel.objects.get(id = catid)
    get_cat.delete()
    return redirect('categoryPage')



@login_required
def categoryEdit(request, catid):
    get_cat = categoryModel.objects.get(id = catid)
    print(get_cat)
    return render(request, 'categoryEdit.html', {'target_cat': get_cat})




@login_required
def categoryUpadte(request):
    if request.method=='POST':
        category_id=request.POST.get('catid')
        category_name=request.POST.get('catName')
        
        save_category = categoryModel(
            id=category_id,
            name = category_name,
        )
        save_category.save()
        return redirect('categoryPage')




@login_required
def subCategoryForm(request):
    allcategory=categoryModel.objects.all()

    if request.method=='POST':
        catid=request.POST.get('catid')
        Id = get_object_or_404(categoryModel, id=catid)
        subcatid=request.POST.get('subCatid')

        save_sub_category = sub_categoryModel(
            category=Id,
            name=subcatid,
        )
        save_sub_category.save()
        return redirect('categoryPage')
    
    return render(request, "subCategoryForm.html", {'allcat': allcategory})



@login_required
def subCategoryDelete(request, subCatid):
    get_cat = sub_categoryModel.objects.get(id = subCatid)
    get_cat.delete()
    return redirect('categoryPage')




@login_required
def subCategoryEdit(request, subCatid):
    get_subCat = sub_categoryModel.objects.get(id = subCatid)
    print(get_subCat)
    return render(request, 'subCategoryEdit.html', {'target_subcat': get_subCat})



@login_required
def subCategoryUpadte(request):
    if request.method=='POST':
        subCategory_id=request.POST.get('subCatid')
        uCat=request.POST.get('uCat')
        uCatobj = get_object_or_404(categoryModel, id=uCat)
        subCategory_name=request.POST.get('subCatName')
        print(subCategory_name)
        save_subCategory = sub_categoryModel(
            id=subCategory_id,
            category=uCatobj,
            name = subCategory_name,
        )
        save_subCategory.save()
        return redirect('categoryPage')







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
