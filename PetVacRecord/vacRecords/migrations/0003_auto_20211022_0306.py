# Generated by Django 3.2.8 on 2021-10-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacRecords', '0002_alter_checkup_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkup',
            name='checkupNotes',
        ),
        migrations.AddField(
            model_name='checkup',
            name='checkupnotes',
            field=models.TextField(null=True, verbose_name=''),
        ),
    ]