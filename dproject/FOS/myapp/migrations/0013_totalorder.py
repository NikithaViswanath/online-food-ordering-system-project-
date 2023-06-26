# Generated by Django 4.1 on 2022-09-09 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_recipie_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='totalorder',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.CharField(blank=True, default='', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('totalamount', models.IntegerField(default='')),
            ],
        ),
    ]