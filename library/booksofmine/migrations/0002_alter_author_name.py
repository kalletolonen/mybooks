# Generated by Django 3.2 on 2022-05-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksofmine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
    ]