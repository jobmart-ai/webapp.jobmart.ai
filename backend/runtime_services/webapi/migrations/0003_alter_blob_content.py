# Generated by Django 3.2.12 on 2024-05-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0002_auto_20240503_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blob',
            name='content',
            field=models.BinaryField(editable=True),
        ),
    ]
