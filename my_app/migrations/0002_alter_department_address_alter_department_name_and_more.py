# Generated by Django 4.2.5 on 2023-09-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
