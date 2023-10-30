# Generated by Django 3.2.8 on 2023-07-09 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0002_auto_20230708_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='answer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='question',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='qnat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True)),
                ('answer', models.TextField(blank=True)),
                ('usr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
