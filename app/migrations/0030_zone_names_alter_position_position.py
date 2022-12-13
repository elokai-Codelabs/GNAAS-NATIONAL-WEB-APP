# Generated by Django 4.1.3 on 2022-12-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_fellowship_fellowship_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone_Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.CharField(max_length=100),
        ),
    ]