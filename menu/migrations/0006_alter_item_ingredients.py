# Generated by Django 4.2 on 2023-04-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ingredients',
            field=models.ManyToManyField(default=None, to='menu.ingredient'),
        ),
    ]
