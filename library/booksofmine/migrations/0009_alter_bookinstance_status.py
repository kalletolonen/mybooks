# Generated by Django 3.2 on 2022-05-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksofmine', '0008_bookinstance_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='o', help_text='Book availability', max_length=1),
        ),
    ]
