# Generated by Django 3.2 on 2022-09-26 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0032_favouritejob'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Remote', 'Remote')], max_length=200, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobseeker',
            name='looking_for',
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='looking_for',
            field=models.ManyToManyField(max_length=200, to='jobs.JobType'),
        ),
    ]
