# Generated by Django 4.1.3 on 2022-12-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_zone_union_coordinating_secretary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='phone',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
