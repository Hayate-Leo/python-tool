# Generated by Django 3.2.3 on 2021-05-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('re_area', models.CharField(blank=True, max_length=100, null=True)),
                ('re_rate', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
