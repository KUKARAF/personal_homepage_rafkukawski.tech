# Generated by Django 3.1.3 on 2021-01-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('painting_name', models.CharField(max_length=50)),
                ('painting_author', models.CharField(max_length=30)),
                ('painting_date', models.DateField()),
                ('painting_id', models.AutoField(primary_key=True, serialize=False)),
                ('painting_price', models.CharField(max_length=10)),
                ('painting_desc', models.CharField(max_length=300)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
