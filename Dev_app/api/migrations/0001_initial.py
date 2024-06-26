# Generated by Django 4.2.9 on 2024-04-06 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('imageUrl', models.ImageField(upload_to='pendingTask')),
                ('isCompleted', models.BooleanField(default=False)),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetailTesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('activEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usedetail', to='api.email')),
            ],
        ),
    ]
