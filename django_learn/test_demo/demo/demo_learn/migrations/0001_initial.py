# Generated by Django 2.2.5 on 2019-10-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoubandbMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.CharField(blank=True, max_length=10, null=True)),
                ('info', models.CharField(blank=True, max_length=100, null=True)),
                ('movie_site', models.CharField(blank=True, max_length=100, null=True)),
                ('pic_site', models.CharField(blank=True, max_length=100, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True, verbose_name='导演')),
                ('actor', models.CharField(blank=True, max_length=50, null=True, verbose_name='演员')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('color_code', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'db_table': 'doubandb_movies',
                'managed': False,
            },
        ),
    ]
