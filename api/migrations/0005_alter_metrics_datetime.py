# Generated by Django 4.0.2 on 2022-03-16 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_metrics_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]