# Generated by Django 3.2 on 2022-07-26 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='phoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile', models.IntegerField()),
                ('isVerified', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RateGroup',
            fields=[
                ('rate_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('rate_group_name', models.CharField(help_text=' Name of a rate card group', max_length=255)),
            ],
            options={
                'db_table': 'rate_group',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format +919999999999. Up to 14 digits allowed.', regex='^\\+?1?\\d{9,10}$')])),
                ('alternate_number', models.CharField(blank=True, max_length=30, null=True)),
                ('active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('superuser', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user_type', models.CharField(choices=[('staff', 'staff'), ('Freelancer', 'Freelancer')], max_length=255)),
                ('date_of_birth', models.DateField(blank=True, help_text='date format: yyyy-mm-dd    ex:2018-11-15', null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
