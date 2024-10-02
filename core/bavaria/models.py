from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    USER=[
        ('administrator', 'Administrator'), ('manager', 'Manager'), ('editor', 'Editor')
    ]
    dob=models.CharField(max_length=100, null=True)
    gender=models.CharField(max_length=100, null=True)
    user_role=models.CharField(choices=USER, max_length=100, null=True)
    image=models.ImageField(upload_to="static/media/reg", null=True)



class categoryModel(models.Model):
    name=models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name
    

class sub_categoryModel(models.Model):
    category=models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name
    
class brandNmaeModel(models.Model):
    category=models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True)
    subcategory=models.ForeignKey(sub_categoryModel, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name
    


class Order(models.Model):
    # CATEGORY_CHOICES = [
    #     ('textiles', 'Textiles'),
    #     ('garments', 'Garments'),
    #     ('accessories', 'Accessories'),
    #     # Add more categories as needed
    # ]

    # SUBCATEGORY_CHOICES = [
    #     ('t-shirts', 'T-Shirts'),
    #     ('hoodies', 'Hoodies'),
    #     ('caps', 'Caps'),
    #     # Add more sub-categories as needed
    # ]

    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(sub_categoryModel, on_delete=models.CASCADE, null=True)
    order_reference = models.CharField(max_length=50, unique=True)
    order_date = models.DateField(null=True)
    delivery_date = models.DateField(null=True)
    name = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField(null=True)

    
    budget_plan = models.CharField(max_length=30, default="Pending", null=True)

    # Fields related to machine operations
    machine_layout = models.CharField(max_length=30, default="Pending", null=True)
    machine_report = models.CharField(max_length=30, default="Pending", null=True)

    # Process steps
    purchase = models.CharField(max_length=30, default="Pending", null=True)
    embroidery = models.CharField(max_length=30, default="Pending", null=True)
    sewing = models.CharField(max_length=30, default="Pending", null=True)
    production = models.CharField(max_length=30, default="Pending", null=True)
    quality_check = models.CharField(max_length=30, default="Pending", null=True)
    ironing = models.CharField(max_length=100, default="Pending", null=True)
    packing = models.CharField(max_length=30, default="Pending", null=True)
    shipping = models.CharField(max_length=30, default="Pending", null=True)

    # Stock management
    stock = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.order_reference}"





class budgetPlaning(models.Model):
    date = models.DateField(null=True)
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(sub_categoryModel, on_delete=models.CASCADE, null=True)
    order_reference = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    marker_cost = models.IntegerField(null=True)
    cutting_cost = models.IntegerField(null=True)
    sewing_cost = models.IntegerField(null=True)
    quality_check = models.IntegerField(null=True)
    ironing = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    budget_cost = models.IntegerField(null=True)
    actual_cost = models.IntegerField(null=True)
    qty = models.IntegerField(null=True)
    status=models.CharField(max_length=30, default="Pending", null=True)




    # def total_cost(self):
    #     """Calculate total costs based on individual costs and quantity."""
    #     costs = [
    #         self.marker_cost or 0,
    #         self.cutting_cost or 0,
    #         self.sewing_cost or 0,
    #         self.quality_check or 0,
    #         self.ironing or 0,
    #         self.packing_cost or 0,
    #     ]
    #     return sum(costs) * (self.qty or 0)

    # def is_within_budget(self):
    #     """Check if actual cost is within budget."""
    #     return (self.actual_cost or 0) <= (self.budget_cost or 0)

    # def __str__(self):
    #     return f"Order {self.order_reference} - {self.name}"
