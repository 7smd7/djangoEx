# Generated by Django 3.2.7 on 2021-10-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangement_advertiser', '0002_auto_20211006_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]