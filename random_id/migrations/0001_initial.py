# Generated by Django 3.2.3 on 2021-05-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_uuid', models.CharField(max_length=150)),
                ('time_created', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Random ID',
                'verbose_name_plural': 'Random IDs',
            },
        ),
    ]