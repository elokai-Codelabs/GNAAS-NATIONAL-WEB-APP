# Generated by Django 4.1.3 on 2022-12-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_year_of_service_executive_date_of_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='committee_member',
            old_name='year_of_service',
            new_name='date_of_service',
        ),
        migrations.AlterField(
            model_name='executive',
            name='leadership_level',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=100),
        ),
    ]
