# Generated by Django 4.2 on 2024-06-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.TextField()),
                ('student_age', models.IntegerField()),
                ('student_place', models.CharField(max_length=100)),
                ('student_class', models.CharField(max_length=100)),
            ],
        ),
    ]
