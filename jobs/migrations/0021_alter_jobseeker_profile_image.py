# Generated by Django 3.2 on 2022-09-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_jobposting_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='profile_image',
            field=models.ImageField(blank=True, default='default/1.png', null=True, upload_to='profileimage'),
        ),
    ]
