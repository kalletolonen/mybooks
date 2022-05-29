# Generated by Django 3.2 on 2022-05-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksofmine', '0005_alter_bookinstance_due_back'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
