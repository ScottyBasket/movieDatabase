# Generated by Django 4.2.6 on 2023-11-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='name2',
            field=models.CharField(max_length=255, null=True, verbose_name='name2'),
        ),
    ]