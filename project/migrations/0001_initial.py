# Generated by Django 4.0 on 2021-12-17 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=30)),
                ('project_phase', models.CharField(blank=True, max_length=30, null=True)),
                ('building_name', models.CharField(max_length=50)),
                ('building_type', models.CharField(max_length=50)),
                ('total_apartments', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_no', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('floor_no', models.CharField(max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('profiles', models.IntegerField()),
                ('building_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.building')),
            ],
        ),
    ]