# Generated by Django 5.1.2 on 2024-11-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='business_name',
            field=models.CharField(max_length=122, unique=True),
        ),
    ]
