# Generated by Django 4.2.5 on 2023-09-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_employee_department_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='receipt_date',
            field=models.DateTimeField(),
        ),
    ]