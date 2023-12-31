# Generated by Django 4.1.4 on 2023-01-07 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('phone', models.BigIntegerField(max_length=64)),
                ('about', models.TextField(max_length=64)),
                ('position', models.CharField(choices=[('manager', 'manager'), ('software_developer', 'software_developer'), ('trainer', 'trainer')], max_length=64)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
