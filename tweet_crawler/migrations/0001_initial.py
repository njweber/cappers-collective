# Generated by Django 3.1.3 on 2021-01-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweets_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.TextField(max_length=50)),
                ('text', models.TextField()),
                ('url', models.TextField()),
                ('status_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tweets_all',
            },
        ),
        migrations.CreateModel(
            name='tweets_bets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.TextField(max_length=50)),
                ('text', models.TextField()),
                ('url', models.TextField()),
                ('status_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tweets_bets',
            },
        ),
        migrations.CreateModel(
            name='twitter_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'twitter_users',
            },
        ),
    ]