# Generated by Django 4.2.2 on 2023-06-13 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
    ]
