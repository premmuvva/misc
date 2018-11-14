# Generated by Django 2.1.3 on 2018-11-08 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magzapp', '0006_auto_20181108_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('magazine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magzapp.Magazine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]