# Generated by Django 4.2 on 2023-04-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_menucategory_category_rename_menuitem_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='item',
            name='ingredients',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='menu.ingredient'),
        ),
    ]
