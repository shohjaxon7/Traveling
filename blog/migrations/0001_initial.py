# Generated by Django 5.1.6 on 2025-02-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('price', models.FloatField(blank=True)),
                ('text', models.TextField()),
                ('text1', models.TextField()),
            ],
        ),
    ]
