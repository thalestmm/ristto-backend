# Generated by Django 4.2 on 2023-05-21 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_alter_restaurant_owner_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
