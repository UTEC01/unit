# Generated by Django 3.2 on 2021-04-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0006_post_出荷日'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='c_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='出荷日',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='購入納期',
            field=models.DateField(blank=True, null=True),
        ),
    ]