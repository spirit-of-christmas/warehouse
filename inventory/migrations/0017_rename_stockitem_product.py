# Generated by Django 3.2 on 2021-04-25 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('inventory', '0016_remove_stockitem_barcode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockItem',
            new_name='Product',
        ),
    ]
