""" Версия 2 VPS с выбором параметров из .csv файлов. """
import uuid

from django.db import models
import csv

"""
Объект VPS

• uid - идентификатор

• cpu - количество ядер

• ram - объем RAM

• hdd - объем HDD

• status - статус сервера (started, blocked, stopped)
"""

CPU = []
RAM = []
HDD = []

with open('static/cpu.csv', 'r') as cpu_file:
    cpu = csv.reader(cpu_file)
    for i in cpu:
        cpu_t = (i[0], i[0])
        CPU.append(cpu_t)

with open('static/ram.csv', 'r') as ram_file:
    ram = csv.reader(ram_file)
    for i in ram:
        ram_t = (i[0], i[0])
        RAM.append(ram_t)

with open('static/hdd.csv', 'r') as hdd_file:
    hdd = csv.reader(hdd_file)
    for i in hdd:
        hdd_t = (i[0], i[0])
        HDD.append(hdd_t)


class VPS(models.Model):
    """ Модель VPS"""
    SERVER_STATUS = [
        ('started', 'started'),
        ('blocked', 'blocked'),
        ('stopped', 'stopped'),
    ]
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.CharField(max_length=2, choices=CPU, verbose_name='ядер шт')
    ram = models.CharField(max_length=2, choices=RAM, verbose_name='озу Гб')
    hdd = models.CharField(max_length=2, choices=HDD, verbose_name='hdd Тб')
    status = models.CharField(max_length=7, choices=SERVER_STATUS, verbose_name='статус сервера')
