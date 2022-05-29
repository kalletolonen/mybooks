# Generated by Django 3.2 on 2022-05-29 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksofmine', '0006_bookinstance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='loan_date',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]