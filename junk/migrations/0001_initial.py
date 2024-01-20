# Generated by Django 5.0.1 on 2024-01-08 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='uploads/courses/')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Loop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date published')),
                ('wage', models.IntegerField()),
                ('bags', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junk.group')),
            ],
        ),
        migrations.CreateModel(
            name='LoopCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junk.course')),
                ('loop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junk.loop')),
            ],
        ),
        migrations.AddField(
            model_name='loop',
            name='courses',
            field=models.ManyToManyField(through='junk.LoopCourse', to='junk.course'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('lon', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='uploads/people/')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junk.group')),
            ],
        ),
    ]
