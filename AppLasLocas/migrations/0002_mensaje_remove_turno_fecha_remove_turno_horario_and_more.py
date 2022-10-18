# Generated by Django 4.1 on 2022-10-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLasLocas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='turno',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='horario',
        ),
        migrations.AddField(
            model_name='servicio',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turno',
            name='mensaje',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='costo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='horarios',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='servicio',
            field=models.CharField(max_length=200),
        ),
    ]