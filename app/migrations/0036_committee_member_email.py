# Generated by Django 4.1.3 on 2022-12-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_alumni_rep_zone_alter_chaplain_zone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee_member',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
