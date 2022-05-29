# Generated by Django 3.2 on 2022-05-29 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksofmine', '0002_alter_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksofmine.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksofmine.book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksofmine.genre')),
            ],
        ),
    ]