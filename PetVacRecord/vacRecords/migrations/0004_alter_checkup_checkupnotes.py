# Generated by Django 3.2.8 on 2021-10-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacRecords', '0003_auto_20211022_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkup',
            name='checkupnotes',
            field=models.TextField(verbose_name=''),
        ),
    ]
