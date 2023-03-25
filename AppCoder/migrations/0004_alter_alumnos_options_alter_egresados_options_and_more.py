# Generated by Django 4.1.7 on 2023-03-24 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0003_alumnos_institucional_profesores_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={'ordering': ['usuario', 'padron']},
        ),
        migrations.AlterModelOptions(
            name='egresados',
            options={'ordering': ['usuario', 'profesion']},
        ),
        migrations.AlterModelOptions(
            name='institucional',
            options={'ordering': ['usuario', 'cargo']},
        ),
        migrations.AlterModelOptions(
            name='profesores',
            options={'ordering': ['usuario', 'materia']},
        ),
        migrations.AddField(
            model_name='alumnos',
            name='fotodni',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='egresados',
            name='fotodni',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AddField(
            model_name='egresados',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='institucional',
            name='fotodni',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AddField(
            model_name='institucional',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profesores',
            name='fotodni',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AddField(
            model_name='profesores',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='egresados',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='egresados',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='egresados',
            name='profesion',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='institucional',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='institucional',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='materia',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='AppCoder.alumnos')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
