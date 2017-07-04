# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(verbose_name='Дата добавления комментария')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='Текст записи'),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
        ),
    ]