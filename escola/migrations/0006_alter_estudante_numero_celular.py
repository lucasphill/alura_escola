# Generated by Django 5.0.9 on 2024-09-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0005_alter_estudante_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='numero_celular',
            field=models.CharField(max_length=14),
        ),
    ]