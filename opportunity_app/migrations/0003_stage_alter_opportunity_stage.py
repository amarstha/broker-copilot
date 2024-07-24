# Generated by Django 5.0.6 on 2024-07-24 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity_app', '0002_opportunity_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opportunities', to='opportunity_app.stage'),
        ),
    ]
