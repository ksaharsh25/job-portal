# Generated by Django 3.2 on 2022-10-11 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
        ('jobs', '0038_auto_20221011_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.country'),
        ),
    ]
