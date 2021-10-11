# Generated by Django 3.2.7 on 2021-10-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangement_advertiser', '0016_alter_ad_advertiser'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('keyTime', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=10)),
                ('count', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HourlyReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('keyTime', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=10)),
                ('count', models.BigIntegerField()),
            ],
        ),
    ]