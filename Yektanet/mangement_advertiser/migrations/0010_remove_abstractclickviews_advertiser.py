# Generated by Django 3.2.7 on 2021-10-09 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangement_advertiser', '0009_auto_20211009_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstractclickviews',
            name='advertiser',
        ),
    ]