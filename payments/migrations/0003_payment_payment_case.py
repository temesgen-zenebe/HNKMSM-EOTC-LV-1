# Generated by Django 4.2 on 2024-06-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_billinginformation_paymentcasecartlist_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_case',
            field=models.CharField(blank=True, null=True),
        ),
    ]
