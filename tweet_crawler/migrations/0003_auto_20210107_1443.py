# Generated by Django 3.1.3 on 2021-01-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_crawler', '0002_auto_20201107_1837'),
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
            ],
            options={
                'db_table': 'tweets_bets',
            },
        ),
        migrations.DeleteModel(
            name='tweet',
        ),
    ]
