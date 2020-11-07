# Generated by Django 3.1.3 on 2020-11-07 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'tweet',
            },
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]