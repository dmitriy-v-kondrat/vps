"""Версия 3 VPS с моделями cpu, ram, hdd. Для создания, редактирования и удаления доступных вариантов из админки. """
import uuid

from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

"""
Объект VPS

• uid - идентификатор

• cpu - количество ядер

• ram - объем RAM

• hdd - объем HDD

• status - статус сервера (started, blocked, stopped)
"""


class CPU(models.Model):
    cpu_p = models.PositiveSmallIntegerField(validators=[MaxValueValidator(64)], verbose_name='ядро шт', unique=True)

    def __str__(self):
        return str(self.cpu_p)

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPU'


class RAM(models.Model):
    ram_p = models.PositiveSmallIntegerField(validators=[MaxValueValidator(512)], verbose_name='озу гб', unique=True)

    def __str__(self):
        return str(self.ram_p)

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAM'


class HDD(models.Model):
    hdd_p = models.PositiveSmallIntegerField(validators=[MaxValueValidator(16)], verbose_name='hdd тб', unique=True)

    def __str__(self):
        return str(self.hdd_p)

    class Meta:
        verbose_name = 'HDD'
        verbose_name_plural = 'HDD'


class VPS(models.Model):
    """ Модель VPS"""
    SERVER_STATUS = [
        ('started', 'started'),
        ('blocked', 'blocked'),
        ('stopped', 'stopped'),
    ]
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, to_field='cpu_p')
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, to_field='ram_p')
    hdd = models.ForeignKey(HDD, on_delete=models.CASCADE, to_field='hdd_p')
    status = models.CharField(max_length=7, choices=SERVER_STATUS, verbose_name='статус сервера')
