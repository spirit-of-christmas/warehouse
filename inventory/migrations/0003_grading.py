# Generated by Django 3.1.4 on 2021-04-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
