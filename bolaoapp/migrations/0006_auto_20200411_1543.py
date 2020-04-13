# Generated by Django 2.2.12 on 2020-04-11 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolaoapp', '0005_aposta_jogador'),
    ]

    operations = [
        migrations.AddField(
            model_name='aposta',
            name='partida',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bolaoapp.Partida'),
        ),
        migrations.AlterField(
            model_name='aposta',
            name='vencedor',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]