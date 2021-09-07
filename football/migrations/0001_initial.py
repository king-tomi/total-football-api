# Generated by Django 3.2.6 on 2021-08-08 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('stadium', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=250)),
                ('away_team', models.CharField(max_length=250)),
                ('home_goals', models.IntegerField()),
                ('away_goals', models.IntegerField()),
                ('winner', models.CharField(max_length=250)),
                ('yellow_cards', models.IntegerField(blank=True, null=True)),
                ('red_cards', models.IntegerField(blank=True, null=True)),
                ('free_kicks', models.IntegerField(blank=True, null=True)),
                ('penalties', models.IntegerField(blank=True, null=True)),
                ('corners', models.IntegerField(blank=True, null=True)),
                ('home_possession', models.IntegerField(blank=True, null=True)),
                ('away_possession', models.IntegerField(blank=True, null=True)),
                ('home_shots', models.IntegerField(blank=True, null=True)),
                ('away_shots', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=100)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.club')),
            ],
        ),
    ]
