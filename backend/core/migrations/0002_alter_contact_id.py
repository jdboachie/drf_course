# Generated by Django 4.1.3 on 2023-10-11 22:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b5eb9644-fa29-49ef-9aa5-9247f82e1a8f'), primary_key=True, serialize=False),
        ),
    ]
