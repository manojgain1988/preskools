# Generated by Django 5.1.5 on 2025-01-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_adddepartment_department_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddepartment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='adddepartment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
