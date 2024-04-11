# Generated by Django 5.0.4 on 2024-04-11 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0009_pizzatemtamanho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tamanho',
            name='preco',
        ),
        migrations.AddField(
            model_name='pizzatemtamanho',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
