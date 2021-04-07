# Generated by Django 3.2 on 2021-04-07 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls_app.poll'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=4096),
        ),
    ]
