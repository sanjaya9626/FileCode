# Generated by Django 3.2.11 on 2023-03-12 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='username', max_length=255, unique=True)),
                ('email', models.CharField(help_text='email', max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('fullname', models.CharField(blank=True, help_text='full name', max_length=255, null=True)),
            ],
        ),
    ]
