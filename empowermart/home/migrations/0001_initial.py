# Generated by Django 5.1.2 on 2024-11-21 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=128)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=200)),
                ('Product_Description', models.TextField()),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('Price_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='home.user')),
            ],
        ),
    ]
