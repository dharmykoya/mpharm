# Generated by Django 2.2.7 on 2019-11-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=500)),
                ('diagnosis_code', models.CharField(max_length=500)),
                ('full_code', models.CharField(max_length=500)),
                ('abbreviated_description', models.CharField(max_length=500)),
                ('full_description', models.CharField(max_length=500)),
                ('category_title', models.CharField(max_length=500)),
            ],
        ),
    ]
