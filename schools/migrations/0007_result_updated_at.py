# Generated by Django 4.2 on 2024-04-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_result_is_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
