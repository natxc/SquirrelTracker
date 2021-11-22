# Generated by Django 3.1.2 on 2020-10-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(help_text='Latitude')),
                ('Longitude', models.FloatField(help_text='Longitude')),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique Squirrel ID', max_length=100, unique=True)),
                ('Shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], max_length=2)),
                ('Date', models.DateField(help_text='Date Sighted')),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age of Squirrel', max_length=30)),
                ('Primary_Fur_Color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary Color of Squirrel', max_length=25)),
                ('Location', models.CharField(choices=[('Ground_Plane', 'Ground_Plane'), ('Above_Ground', 'Above_Ground')], help_text='Location of Squirrel', max_length=40)),
                ('Specific_Location', models.CharField(blank=True, help_text='More specific location of Squirrel', max_length=1000)),
                ('Running', models.BooleanField(default=False, help_text='Is the Squirrel running')),
                ('Chasing', models.BooleanField(default=False, help_text='Is the Squirrel chasing')),
                ('Climbing', models.BooleanField(default=False, help_text='Is the squirrel climbing')),
                ('Eating', models.BooleanField(default=False, help_text='Is the squirrel eating')),
                ('Foraging', models.BooleanField(default=False, help_text='Is the squirrel foraging')),
                ('Other_Activities', models.CharField(blank=True, help_text='Other activies that the squirrel is doing', max_length=1000)),
                ('Kuks', models.BooleanField(default=False, help_text='Does the Squirrel Kuk')),
                ('Quaas', models.BooleanField(default=False, help_text='Does the Squirrel Quaa')),
                ('Moans', models.BooleanField(default=False, help_text='Does the Squirrel Moan')),
                ('Tail_flags', models.BooleanField(default=False, help_text='Does the Squirrel have a tail flag')),
                ('Tail_twitches', models.BooleanField(default=False, help_text='Does the Squirrel tail twitch')),
                ('Approaches', models.BooleanField(default=False, help_text='Does the Squirrel approach you')),
                ('Indifferent', models.BooleanField(default=False, help_text='Is the Squirrel indifferent')),
                ('Runs_from', models.BooleanField(default=False, help_text='Does the Squirrel run from you')),
            ],
        ),
    ]
