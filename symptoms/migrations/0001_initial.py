# Generated by Django 5.1.3 on 2024-12-05 13:52

import datetime
import django.db.models.deletion
import symptoms.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, validators=[symptoms.models.validate_past_date])),
                ('type', models.CharField(choices=[('pain', 'Abdominal Pain'), ('blood', 'Blood in Stool'), ('urgency', 'Urgency'), ('diarrhoea', 'Diarrhoea'), ('fatigue', 'Fatigue'), ('joint_pain', 'Joint Pain'), ('other', 'Other')], default='other', max_length=100)),
                ('severity', models.IntegerField(choices=[(1, 'Very Mild'), (2, 'Mild'), (3, 'Moderate'), (4, 'Severe'), (5, 'Very Severe')])),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
