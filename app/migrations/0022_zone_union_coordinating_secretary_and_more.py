# Generated by Django 4.1.3 on 2022-12-08 23:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_committee_date_of_assumption_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('school_hosting', models.CharField(blank=True, max_length=200, null=True)),
                ('president', models.CharField(blank=True, max_length=200, null=True)),
                ('president_contact', models.IntegerField(blank=True, null=True)),
                ('secretary', models.CharField(blank=True, max_length=200, null=True)),
                ('secretary_contact', models.IntegerField(blank=True, null=True)),
                ('treasurer', models.CharField(blank=True, max_length=200, null=True)),
                ('treasurer_contact', models.IntegerField(blank=True, null=True)),
                ('coordinating_secretary', models.CharField(blank=True, max_length=200, null=True)),
                ('coordinating_secretary_contact', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='union',
            name='coordinating_secretary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='coordinating_secretary_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='president_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='school_hosting',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='secretary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='secretary_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='treasurer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='union',
            name='treasurer_contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='committee',
            name='date_of_assumption',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2022', '2022')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='committee_member',
            name='date_of_service',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2022', '2022')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='date_of_service',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2022', '2022')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='union',
            name='name',
            field=models.CharField(choices=[('SGUC', 'Southern Ghana Union'), ('NGUC', 'Northern Ghana Union')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='union',
            name='president',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('union', models.CharField(blank=True, choices=[('SGUC', 'Southern Ghana Union'), ('NGUC', 'Northern Ghana Union')], max_length=200, null=True)),
                ('president', models.CharField(blank=True, max_length=200, null=True)),
                ('president_contact', models.IntegerField(blank=True, null=True)),
                ('secretary', models.CharField(blank=True, max_length=200, null=True)),
                ('secretary_contact', models.IntegerField(blank=True, null=True)),
                ('treasurer', models.CharField(blank=True, max_length=200, null=True)),
                ('treasurer_contact', models.IntegerField(blank=True, null=True)),
                ('chaplain', models.CharField(blank=True, max_length=200, null=True)),
                ('chaplain_contact', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.zone')),
            ],
        ),
    ]