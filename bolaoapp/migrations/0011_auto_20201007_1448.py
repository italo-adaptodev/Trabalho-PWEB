# Generated by Django 3.1.2 on 2020-10-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolaoapp', '0010_auto_20201007_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='isValidoParaAposta',
            field=models.BooleanField(default=True),
        ),
    ]
