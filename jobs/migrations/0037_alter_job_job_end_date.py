# Generated by Django 3.2 on 2022-10-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0036_alter_job_pin_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
