# Generated by Django 3.0.6 on 2020-05-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_save_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con1', models.CharField(max_length=255)),
                ('con2', models.CharField(max_length=255)),
            ],
        ),
    ]
