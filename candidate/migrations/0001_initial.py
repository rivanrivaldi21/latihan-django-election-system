# Generated by Django 3.2 on 2022-08-13 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Canidate's Name")),
                ('vision', models.TextField(verbose_name="Candidate's Vision")),
                ('mission', models.TextField(verbose_name="Candidate's Mission")),
                ('score', models.IntegerField(verbose_name='Score')),
                ('related_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]