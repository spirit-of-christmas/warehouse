# Generated by Django 3.2 on 2021-04-25 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_rename_grading_quality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockitem',
            old_name='type',
            new_name='category',
        ),
    ]