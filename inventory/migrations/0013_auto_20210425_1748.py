# Generated by Django 3.2 on 2021-04-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_stockitem_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='barcode_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockitem',
            name='barcode',
            field=models.ImageField(upload_to='barcodes/'),
        ),
    ]