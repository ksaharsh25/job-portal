# Generated by Django 3.2 on 2022-08-09 04:48

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Address.country')),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Address.country')),
                ('state', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='Address.state')),
            ],
            options={
                'db_table': 'city',
            },
        ),
    ]
