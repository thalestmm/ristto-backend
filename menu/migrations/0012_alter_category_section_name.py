# Generated by Django 4.2 on 2023-05-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_category_section_name_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='section_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]