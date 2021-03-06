# Generated by Django 3.2.5 on 2021-07-06 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='translator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=50)),
                ('luo', models.CharField(max_length=50)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'translator',
                'verbose_name_plural': 'translators',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='textlang',
        ),
    ]
