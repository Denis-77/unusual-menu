# Generated by Django 4.1.7 on 2023-02-26 11:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
                ('url', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='URL')),
                ('full_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='FULL_URL')),
                ('parent_url', models.CharField(blank=True, max_length=255, null=True, verbose_name="Parent's URL")),
                ('level', models.PositiveIntegerField(default=1, verbose_name='level')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_app.menu')),
            ],
            options={
                'ordering': ('level',),
            },
        ),
    ]
