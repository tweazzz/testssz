# Generated by Django 4.2.7 on 2023-11-30 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prepod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, unique=True)),
                ('photo3x4', models.ImageField(blank=True, null=True, upload_to='')),
                ('short_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('job_characteristic', models.TextField()),
                ('prepod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tts.prepod')),
            ],
        ),
    ]
