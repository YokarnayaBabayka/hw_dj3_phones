# Generated by Django 5.0.6 on 2024-07-09 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=None)),
                ('image', models.URLField(default=None)),
                ('release_date', models.DateField(default=None)),
                ('lte_exists', models.BooleanField(default=None)),
                ('slug', models.SlugField(max_length=70, unique=True)),
            ],
        ),
    ]
