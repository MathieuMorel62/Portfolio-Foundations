# Generated by Django 4.2.2 on 2023-06-13 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='category.category'),
        ),
    ]
