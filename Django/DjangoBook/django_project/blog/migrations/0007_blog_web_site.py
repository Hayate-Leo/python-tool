# Generated by Django 3.2.7 on 2021-10-23 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_contact_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='web_site',
            field=models.URLField(blank=True),
        ),
    ]