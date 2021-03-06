# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-05 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myquestion', '0002_questionnaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='题纲', max_length=128)),
                ('index', models.IntegerField(db_index=True, default=0, help_text='题目题号')),
                ('category', models.CharField(choices=[('radio', '单选'), ('select', '多选')], default='radio', help_text='是否多选', max_length=16)),
                ('questionnaire', models.ForeignKey(help_text='问卷', on_delete=django.db.models.deletion.CASCADE, to='Myquestion.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='选项内容', max_length=32)),
                ('question', models.ForeignKey(help_text='题目', on_delete=django.db.models.deletion.CASCADE, to='Myquestion.Question')),
            ],
        ),
    ]
