# Generated by Django 4.2 on 2023-04-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_category_options_alter_item_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]