# Generated by Django 3.2 on 2021-04-23 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0017_minyuka_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minyuka',
            old_name='ID',
            new_name='m_id',
        ),
    ]