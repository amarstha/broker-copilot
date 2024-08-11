# Generated by Django 5.0.6 on 2024-08-03 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemPrompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_purpose', models.TextField(blank=True, null=True)),
                ('applicant_overview', models.TextField(blank=True, null=True)),
                ('living_condition', models.TextField(blank=True, null=True)),
                ('employment_income', models.TextField(blank=True, null=True)),
                ('commitments', models.TextField(blank=True, null=True)),
                ('others', models.TextField(blank=True, null=True)),
                ('mitigants', models.TextField(blank=True, null=True)),
            ],
        ),
    ]