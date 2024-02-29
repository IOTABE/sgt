# Generated by Django 5.0.1 on 2024-01-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='veiculo',
            name='odometro',
            field=models.IntegerField(default=0),
        ),
    ]