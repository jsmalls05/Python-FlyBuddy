# Generated by Django 2.2.4 on 2020-09-23 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desti', models.CharField(max_length=255)),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('endDate', models.DateTimeField(auto_now_add=True)),
                ('plan', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fav', models.ManyToManyField(related_name='trips', to='examPartTwoApp.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest', to='examPartTwoApp.User')),
            ],
        ),
    ]
