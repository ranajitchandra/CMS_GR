# Generated by Django 5.1.1 on 2024-09-22 10:30

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dob', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('user_role', models.CharField(choices=[('administrator', 'Administrator'), ('manager', 'Manager'), ('editor', 'Editor')], max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/media/reg')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='sub_categoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bavaria.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_reference', models.CharField(max_length=100, unique=True)),
                ('order_date', models.DateField(null=True)),
                ('delivery_date', models.DateField(null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('budget_plan', models.CharField(default='Pending', max_length=30, null=True)),
                ('machine_layout', models.CharField(default='Pending', max_length=30, null=True)),
                ('machine_report', models.CharField(default='Pending', max_length=30, null=True)),
                ('purchase', models.CharField(default='Pending', max_length=30, null=True)),
                ('embroidery', models.CharField(default='Pending', max_length=30, null=True)),
                ('sewing', models.CharField(default='Pending', max_length=30, null=True)),
                ('production', models.CharField(default='Pending', max_length=30, null=True)),
                ('quality_check', models.CharField(default='Pending', max_length=30, null=True)),
                ('ironing', models.CharField(default='Pending', max_length=100, null=True)),
                ('packing', models.CharField(default='Pending', max_length=30, null=True)),
                ('shipping', models.CharField(default='Pending', max_length=30, null=True)),
                ('stock', models.PositiveIntegerField(default=0, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bavaria.categorymodel')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bavaria.sub_categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='budgetPlaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('marker_cost', models.IntegerField(null=True)),
                ('cutting_cost', models.IntegerField(null=True)),
                ('sewing_cost', models.IntegerField(null=True)),
                ('quality_check', models.IntegerField(null=True)),
                ('ironing', models.IntegerField(null=True)),
                ('packing_cost', models.IntegerField(null=True)),
                ('budget_cost', models.IntegerField(null=True)),
                ('actual_cost', models.IntegerField(null=True)),
                ('qty', models.IntegerField(null=True)),
                ('status', models.CharField(default='Pending', max_length=30, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bavaria.categorymodel')),
                ('order_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bavaria.order')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bavaria.sub_categorymodel')),
            ],
        ),
    ]