# Generated by Django 5.1.1 on 2024-10-20 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bavaria', '0002_order_brandmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_categorymodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='bavaria.categorymodel'),
        ),
    ]