"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bavaria.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', base, name='base'),
    path('home', home, name='home'),
    path('signupPage/', signupPage, name='signupPage'),
    path('', signin, name='signin'),
    path('logoutpage', logoutpage, name='logoutpage'),
    # category Routing,
    path('categoryPage/', categoryPage, name='categoryPage'),
    path('categoryDelete/<int:catid>', categoryDelete, name='categoryDelete'),
    path('categoryEdit/<int:catid>', categoryEdit, name='categoryEdit'),
    path('categoryUpadte/', categoryUpadte, name='categoryUpadte'),

    path('categoryForm/', categoryForm, name='categoryForm'),
    path('subCategoryForm/', subCategoryForm, name='subCategoryForm'),
    path('subCategoryDelete/<int:subCatid>', subCategoryDelete, name='subCategoryDelete'),
    path('subCategoryEdit/<int:subCatid>', subCategoryEdit, name='subCategoryEdit'),
    path('subCategoryUpadte/', subCategoryUpadte, name='subCategoryUpadte'),

    # Order Routing,
    path('orderSummery/', orderSummery, name='orderSummery'),
    path('orderForm/', orderForm, name='orderForm'),

    # Budget Routing,
    path('budget_planing/', budget_planing, name='budget_planing'),
    path('budgetForm/', budgetForm, name='budgetForm'),
    path('budgetStart/<int:myid>', budgetStart, name='budgetStart'),
    path('onGoing/<int:myid>', onGoing, name='onGoing'),
    path('budgetEnd/<int:myid>', budgetEnd, name='budgetEnd'),
    path('ab/', ab, name='ab'),
]
