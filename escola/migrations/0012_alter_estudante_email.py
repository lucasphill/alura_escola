# Generated by Django 5.0.9 on 2024-09-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0011_alter_curso_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]