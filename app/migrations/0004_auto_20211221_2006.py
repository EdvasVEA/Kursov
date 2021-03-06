# Generated by Django 2.2.25 on 2021-12-21 17:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20211221_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Название')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 21, 20, 6, 49, 327448), verbose_name='Добавлен')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'продукт каталога (Пицца)',
                'verbose_name_plural': 'продукт каталога (Пицца)',
                'db_table': 'Pizzaposts',
                'ordering': ['-posted'],
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 21, 20, 6, 49, 326450), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 21, 20, 6, 49, 327448), verbose_name='Дата'),
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
    ]
