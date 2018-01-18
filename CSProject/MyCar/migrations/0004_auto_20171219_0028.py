# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyCar', '0003_auto_20171218_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='name',
            field=models.CharField(default='', max_length=25, verbose_name='Арендатор'),
        ),
        migrations.AddField(
            model_name='rent',
            name='phone',
            field=models.CharField(default='', max_length=11, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='modelcar',
            name='id_fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCar.Fuel', verbose_name='Топливо'),
        ),
        migrations.AlterField(
            model_name='modelcar',
            name='id_rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCar.Rank', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='modelcar',
            name='mark_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCar.Mark', verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='id_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCar.ModelCar', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='id_operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCar.Operator', verbose_name='Оператор'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='id_tariff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCar.Tariff', verbose_name='Тариф'),
        ),
    ]
