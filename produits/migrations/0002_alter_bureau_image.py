# Generated by Django 5.1.7 on 2025-03-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureau',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
