# Generated by Django 3.2.9 on 2021-12-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BZU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_id', models.IntegerField(max_length=11)),
                ('protein', models.FloatField()),
                ('zhiri', models.FloatField()),
                ('uglevodi', models.FloatField()),
            ],
            options={
                'db_table': 'fruits',
                'managed': False,
            },
        ),
    ]
