# Generated by Django 3.2 on 2022-09-16 10:35

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0029_alter_applicant_staff_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='looking_for',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Remote', 'Remote')], max_length=30, null=True),
        ),
    ]
