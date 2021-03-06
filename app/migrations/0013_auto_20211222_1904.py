# Generated by Django 2.2.25 on 2021-12-22 16:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20211222_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 35741), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 39729), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 36737), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='roll',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 38732), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='sup',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 37735), verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 39729), verbose_name='Добавлен'),
        ),
        migrations.CreateModel(
            name='CommentZ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Напишите, что вы хотите заказать, и ваши личные пожелания к заказу')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 19, 4, 9, 40726), verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы клиентов',
                'db_table': 'CommentsZ',
                'ordering': ['-date'],
            },
        ),
    ]
