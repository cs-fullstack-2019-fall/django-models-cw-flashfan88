# Generated by Django 2.0.6 on 2019-09-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startapp1', '0002_auto_20190924_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=100)),
                ('RealName', models.CharField(max_length=100)),
                ('accountNumber', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('color', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='BankEmployees',
        ),
        migrations.DeleteModel(
            name='BankUser',
        ),
    ]
