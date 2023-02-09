# Generated by Django 3.2 on 2022-10-12 05:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0044_auto_20221011_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='about_company',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='about_company',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='about_me',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]