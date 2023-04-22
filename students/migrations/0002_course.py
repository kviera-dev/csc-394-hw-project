# Generated by Django 4.2 on 2023-04-22 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=3)),
                ('students', models.ManyToManyField(to='students.student')),
            ],
        ),
    ]
