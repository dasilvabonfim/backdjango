# Generated by Django 5.0.1 on 2024-04-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_alter_react_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
            ],
        ),
    ]
