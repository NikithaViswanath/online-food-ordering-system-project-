# Generated by Django 4.1 on 2022-08-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_recipie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipie',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]
