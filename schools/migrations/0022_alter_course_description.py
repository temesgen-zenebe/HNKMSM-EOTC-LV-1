# Generated by Django 4.2 on 2024-06-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0021_alter_course_school_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
