# Generated by Django 4.1.4 on 2023-01-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(max_length=255)),
                ('author', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField(max_length=2048)),
                ('address', models.CharField(max_length=200)),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('category', models.TextField(max_length=255)),
            ],
        ),
    ]
