# Generated by Django 4.0.2 on 2022-03-01 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_for_bot_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'City'},
        ),
        migrations.AlterModelOptions(
            name='for_bot',
            options={'verbose_name': 'For_Bot', 'verbose_name_plural': 'For_Bot'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Person'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Place', 'verbose_name_plural': 'Place'},
        ),
    ]
