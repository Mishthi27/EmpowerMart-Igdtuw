# Generated by Django 5.1.2 on 2024-11-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_user_business_name_customuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
