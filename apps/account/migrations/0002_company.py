# Generated by Django 2.2a1 on 2019-02-24 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('account', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Razão Social')),
                (
                    'owner',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='companies',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        )
    ]
