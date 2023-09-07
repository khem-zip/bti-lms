# Generated by Django 4.2.5 on 2023-09-07 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batches'},
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userauth.batch'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='pp',
            field=models.ImageField(blank=True, null=True, upload_to='pp'),
        ),
    ]
