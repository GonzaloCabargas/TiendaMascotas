# Generated by Django 4.0.4 on 2022-06-17 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'felicitaciones']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.IntegerField(verbose_name='id producto')),
                ('nombre_prod', models.CharField(max_length=50, verbose_name='nombre producto')),
                ('descripcion', models.TextField(verbose_name='descripcion')),
                ('valor', models.IntegerField(verbose_name='valor')),
                ('imagen', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False, verbose_name='id usuario')),
                ('nombre_user', models.CharField(max_length=50, verbose_name='nombre usuario')),
                ('apellido', models.TextField(verbose_name='apellido')),
                ('correo', models.CharField(max_length=100, verbose_name='correo')),
                ('contrasena', models.CharField(max_length=20, verbose_name='contrasena')),
                ('imagen', models.ImageField(null='true', upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vta', models.IntegerField(verbose_name='id de la venta')),
                ('neto_vta', models.IntegerField(verbose_name='neto')),
                ('impuesto_vta', models.IntegerField(verbose_name='impuesto')),
                ('total_vta', models.IntegerField(verbose_name='total')),
            ],
        ),
        migrations.CreateModel(
            name='venta_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto', verbose_name='id producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.venta', verbose_name='id venta')),
            ],
        ),
    ]