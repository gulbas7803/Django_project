# Generated by Django 4.1.4 on 2023-01-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('it', 'it'), ('non it', 'non it'), ('mobiles phones', 'mobiles phones')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]