# Generated by Django 3.2.8 on 2021-10-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacRecords', '0004_alter_checkup_checkupnotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkup',
            name='checkupnotes',
            field=models.TextField(null=True, verbose_name=''),
        ),
    ]