# Generated by Django 3.2.6 on 2022-04-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=500, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=500, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.CharField(max_length=500, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
    ]