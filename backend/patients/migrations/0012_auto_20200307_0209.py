# Generated by Django 3.0.3 on 2020-03-06 17:09

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('patients', '0011_auto_20200307_0205'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataSources',
            new_name='DataSource',
        ),
    ]