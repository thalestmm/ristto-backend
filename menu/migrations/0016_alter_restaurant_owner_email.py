# Generated by Django 4.2 on 2023-05-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_menu_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='owner_email',
            field=models.EmailField(default='thales@neivus.com', max_length=200),
            preserve_default=False,
        ),
    ]
