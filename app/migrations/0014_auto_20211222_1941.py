# Generated by Django 2.2.25 on 2021-12-22 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20211222_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 594828), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 596822), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='commentz',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 597820), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 595824), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='roll',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 596822), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='sup',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 595824), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 41, 10, 596822), verbose_name='Добавлен'),
        ),
    ]