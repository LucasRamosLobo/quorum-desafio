# Generated by Django 5.0.3 on 2024-03-10 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quorum_app', '0002_remove_bill_primary_sponsor_bill_sponsor_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Legislator',
        ),
    ]
