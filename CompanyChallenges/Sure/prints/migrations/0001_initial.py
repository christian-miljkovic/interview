# Generated by Django 2.0.3 on 2019-10-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('shipping_cost', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=255)),
            ],
        ),
    ]
