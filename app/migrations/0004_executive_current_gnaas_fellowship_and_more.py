# Generated by Django 4.1.3 on 2022-11-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_full_name_executive_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='current_gnaas_fellowship',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='current_local_church',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='current_local_church_elder',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='current_local_church_elder_contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='current_local_church_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='program_of_study',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='year_of_service',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]