# Generated by Django 5.2 on 2025-05-07 14:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, unique=True)),
                ('cvv', models.CharField(max_length=3)),
                ('expiry_date', models.CharField(default='09/29', max_length=5)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
