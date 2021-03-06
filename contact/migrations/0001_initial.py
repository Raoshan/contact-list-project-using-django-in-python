# Generated by Django 3.2.7 on 2021-11-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500)),
                ('relationship', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
