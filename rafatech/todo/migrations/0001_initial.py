# Generated by Django 3.1.3 on 2020-12-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=30)),
                ('due_date', models.DateField()),
                ('importance', models.IntegerField()),
            ],
        ),
    ]
