# Generated by Django 3.2 on 2021-04-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0016_minyuka_品名'),
    ]

    operations = [
        migrations.AddField(
            model_name='minyuka',
            name='ID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]