# Generated by Django 4.2 on 2024-09-18 01:36

# import ckeditor.fields
from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_web_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            # field=ckeditor.fields.RichTextField(blank=True, null=True),
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
