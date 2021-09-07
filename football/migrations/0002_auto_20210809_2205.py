# Generated by Django 3.2.6 on 2021-08-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='player',
            name='assists',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='dribbles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='goals',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='passes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='reds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='shots',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='yellows',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
