# Generated by Django 3.2 on 2022-10-11 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0040_alter_job_hr_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='job_catagories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.companycategories', verbose_name='job category'),
        ),
    ]
