# Generated by Django 3.2.12 on 2024-06-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blob',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
