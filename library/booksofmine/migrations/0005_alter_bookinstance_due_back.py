# Generated by Django 3.2 on 2022-05-29 14:06

import booksofmine.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksofmine', '0004_auto_20220529_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, default=booksofmine.models.BookInstance.get_duedate, null=True),
        ),
    ]