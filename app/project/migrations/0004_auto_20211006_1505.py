# Generated by Django 3.2.7 on 2021-10-06 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='task_description',
        ),
        migrations.AddField(
            model_name='student',
            name='student_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.userprofile'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_details', models.FileField(upload_to='')),
                ('teacher_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='assignment_upload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.assignment'),
        ),
    ]
