# Generated by Django 4.0.2 on 2022-03-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_metrics_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='datetime',
            field=models.DateTimeField(default='16.03.2022 14:15:53'),
        ),
    ]
