# Generated by Django 4.0.8 on 2022-12-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nasa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nasa',
            name='feet',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nasa',
            name='kilometers',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nasa',
            name='meters',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nasa',
            name='miles',
            field=models.FloatField(),
        ),
    ]
