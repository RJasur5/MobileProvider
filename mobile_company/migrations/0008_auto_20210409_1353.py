# Generated by Django 3.1.7 on 2021-04-09 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_company', '0007_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='numbercode',
        ),
        migrations.AddField(
            model_name='order',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mobile_company.providers'),
        ),
    ]
