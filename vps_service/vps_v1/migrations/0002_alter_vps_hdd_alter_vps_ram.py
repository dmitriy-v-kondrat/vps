# Generated by Django 4.0 on 2022-08-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vps',
            name='hdd',
            field=models.PositiveSmallIntegerField(help_text='Тб', verbose_name='объем HDD'),
        ),
        migrations.AlterField(
            model_name='vps',
            name='ram',
            field=models.PositiveSmallIntegerField(help_text='Гб', verbose_name='объем RAM'),
        ),
    ]
