# Generated by Django 3.1.7 on 2021-04-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_company', '0011_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='order',
            name='phonenumber',
            field=models.ManyToManyField(null=True, to='mobile_company.PhoneNumbers'),
        ),
    ]
