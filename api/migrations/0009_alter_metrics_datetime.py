# Generated by Django 4.0.2 on 2022-03-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_metrics_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
