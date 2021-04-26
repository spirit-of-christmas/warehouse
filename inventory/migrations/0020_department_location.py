# Generated by Django 3.2 on 2021-04-26 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.location'),
        ),
    ]