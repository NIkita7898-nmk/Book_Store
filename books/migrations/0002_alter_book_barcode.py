# Generated by Django 4.2.9 on 2024-01-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='barcode',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
