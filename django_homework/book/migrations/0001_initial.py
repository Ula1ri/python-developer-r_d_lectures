# Generated by Django 4.2 on 2023-04-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('year', models.PositiveSmallIntegerField()),
                ('prise', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
