# Generated by Django 3.2 on 2022-09-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_alter_jobseeker_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycategories',
            name='categories_image',
            field=models.ImageField(default='default/1.png', upload_to='category'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='image',
            field=models.ImageField(default='default/1.png', upload_to='companyimage'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='profile_image',
            field=models.ImageField(default='default/1.png', upload_to='profileimage'),
        ),
    ]
