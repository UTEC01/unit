# Generated by Django 3.2 on 2021-04-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0019_remove_minyuka_m_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='minyuka',
            name='m_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
