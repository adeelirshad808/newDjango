# Generated by Django 3.2.7 on 2021-10-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20211007_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment_details',
            field=models.TextField(null=True),
        ),
    ]