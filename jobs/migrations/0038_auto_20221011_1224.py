# Generated by Django 3.2 on 2022-10-11 06:54

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
        ('jobs', '0037_alter_job_job_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='state', chained_model_field='state', null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.city'),
        ),
        migrations.AlterField(
            model_name='job',
            name='state',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='country', chained_model_field='country', null=True, on_delete=django.db.models.deletion.CASCADE, to='Address.state'),
        ),
    ]
