# Generated by Django 3.2.7 on 2021-10-07 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_assignment_assignment_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.student'),
        ),
    ]