# Generated by Django 3.1.2 on 2020-10-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolaoapp', '0008_auto_20201007_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='qtdGols_time1',
            field=models.IntegerField(blank=True, verbose_name=' GOLS DO TIME 1'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='qtdGols_time2',
            field=models.IntegerField(blank=True, verbose_name=' GOLS DO TIME 2'),
        ),
    ]
