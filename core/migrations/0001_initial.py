# Generated by Django 3.1.2 on 2020-10-16 13:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('results_declared', models.BooleanField(default=False)),
                ('max_team_size', models.IntegerField(default=10)),
                ('max_score', models.IntegerField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team_id', models.CharField(max_length=50)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participating_teams', to='core.hackathon')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_as_a_leader', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='teams_as_a_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'hackathon')},
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField()),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hackathon')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(default='No title provided.', max_length=100)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='core.submission')),
            ],
        ),
    ]