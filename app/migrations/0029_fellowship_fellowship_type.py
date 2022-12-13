# Generated by Django 4.1.3 on 2022-12-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellowship',
            name='fellowship_type',
            field=models.CharField(blank=True, choices=[('University', 'University'), ('Secondary', 'Secondary'), ('Nursing Training', 'Nursing Training'), ('Teacher Training ', 'Teacher Training')], max_length=200, null=True),
        ),
    ]