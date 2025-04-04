# Generated by Django 5.1.6 on 2025-03-06 08:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0002_orgmember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='vision',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='org_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='student',
            name='org',
        ),
        migrations.AddField(
            model_name='organization',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentorg.college'),
        ),
        migrations.AddField(
            model_name='organization',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
