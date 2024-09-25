from django.contrib import admin
from bavaria.models import *

# Register your models here.

class Custom_user_display(admin.ModelAdmin):
    list_display=['username', 'user_role']
admin.site.register(Custom_User, Custom_user_display)


class cat_view(admin.ModelAdmin):
    list_display=['name']

admin.site.register(categoryModel, cat_view)
admin.site.register(sub_categoryModel)
admin.site.register(Order)
admin.site.register(budgetPlaning)


