# Generated by Django 3.2 on 2021-04-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_stockitem_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='barcode',
            field=models.ImageField(default='default.png', upload_to='barcodes/'),
        ),
    ]