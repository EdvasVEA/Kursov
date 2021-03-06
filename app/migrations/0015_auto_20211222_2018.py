# Generated by Django 2.2.25 on 2021-12-22 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20211222_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 359013), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 361006), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='commentz',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 362008), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 360012), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='roll',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 361006), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='sup',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 360012), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 20, 18, 56, 361006), verbose_name='Добавлен'),
        ),
    ]
