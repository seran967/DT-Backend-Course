# Generated by Django 4.0.2 on 2022-02-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_city_place_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='For_Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=70)),
                ('tel', models.CharField(max_length=70)),
                ('user_name', models.CharField(max_length=70)),
                ('inf', models.CharField(max_length=70)),
            ],
        ),
    ]
