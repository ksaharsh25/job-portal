# Generated by Django 3.2 on 2022-08-25 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20220824_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='company_image',
            new_name='image',
        ),
    ]
