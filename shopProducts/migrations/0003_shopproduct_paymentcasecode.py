# Generated by Django 4.2 on 2025-01-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopProducts', '0002_shopproduct_category_shopproduct_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='paymentCaseCode',
            field=models.CharField(blank=True, help_text='if the produce from in OurStore than the paymentCaseCode will be slug of PaymentCases,else leave it blank', max_length=200, null=True),
        ),
    ]
