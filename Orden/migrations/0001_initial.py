# Generated by Django 4.1 on 2022-09-23 01:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modelodedatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=100, verbose_name='dirección')),
                ('lugar', models.IntegerField(choices=[[0, 'Bogota'], [1, 'Mosquera'], [2, 'Tena'], [3, 'La Gran via'], [4, 'La Mesa'], [5, 'San javier']], default=0)),
                ('telefono', models.CharField(blank=True, max_length=10)),
                ('fecha', models.DateTimeField(default=datetime.date.today)),
                ('total', models.IntegerField(null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
        migrations.CreateModel(
            name='CompraItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Orden.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pedido_items', to='modelodedatos.producto')),
            ],
        ),
    ]