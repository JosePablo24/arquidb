# Generated by Django 2.2.1 on 2019-05-31 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_example', models.CharField(max_length=254)),
                ('year_example', models.IntegerField()),
                ('delete_example', models.BooleanField(default=False)),
                ('create_example', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Exampe',
            },
        ),
    ]