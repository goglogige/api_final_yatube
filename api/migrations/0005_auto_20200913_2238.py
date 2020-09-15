# Generated by Django 3.1.1 on 2020-09-13 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200913_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=0, unique='True', verbose_name='slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='api.group'),
        ),
    ]
