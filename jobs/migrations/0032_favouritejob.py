# Generated by Django 3.2 on 2022-09-22 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0031_auto_20220921_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job', verbose_name='JobSeeker')),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobseeker', verbose_name='JobSeeker')),
            ],
            options={
                'unique_together': {('jobseeker', 'job')},
            },
        ),
    ]
