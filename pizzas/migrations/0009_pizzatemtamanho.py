# Generated by Django 5.0.4 on 2024-04-11 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0008_tamanho'),
    ]

    operations = [
        migrations.CreateModel(
            name='pizzaTemTamanho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('react', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.react')),
                ('tamanho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.tamanho')),
            ],
        ),
    ]
