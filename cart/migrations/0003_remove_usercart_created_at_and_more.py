# Generated by Django 4.0.6 on 2023-05-18 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_cart_usercart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='updated_at',
        ),
    ]
