# Generated by Django 4.1.3 on 2022-12-09 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_rename_name_union_full_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='union',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='zone',
            old_name='full_name',
            new_name='name',
        ),
    ]