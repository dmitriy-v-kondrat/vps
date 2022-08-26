# Generated by Django 4.0 on 2022-08-23 12:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpu', models.PositiveSmallIntegerField(help_text='штук', verbose_name='количество ядер')),
                ('ram', models.PositiveSmallIntegerField(verbose_name='объем RAM')),
                ('hdd', models.PositiveSmallIntegerField(verbose_name='объем HDD')),
                ('status', models.CharField(choices=[('started', 'started'), ('blocked', 'blocked'), ('stopped', 'stopped')], max_length=7, verbose_name='статус сервера')),
            ],
        ),
    ]