# Generated by Django 3.2.9 on 2021-12-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0012_auto_20211130_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
