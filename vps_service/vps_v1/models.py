""" Версия VPS с самостоятельным заполнением параметров. """
import uuid

from django.db import models

"""
Объект VPS

• uid - идентификатор

• cpu - количество ядер

• ram - объем RAM

• hdd - объем HDD

• status - статус сервера (started, blocked, stopped)
"""


class VPS(models.Model):
    """ Модель VPS"""
    SERVER_STATUS = [
        ('started', 'started'),
        ('blocked', 'blocked'),
        ('stopped', 'stopped'),
    ]
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.PositiveSmallIntegerField(verbose_name='количество ядер', help_text='штук')
    ram = models.PositiveSmallIntegerField(verbose_name='объем RAM', help_text='Гб')
    hdd = models.PositiveSmallIntegerField(verbose_name='объем HDD', help_text='Тб')
    status = models.CharField(max_length=7, choices=SERVER_STATUS, verbose_name='статус сервера')
