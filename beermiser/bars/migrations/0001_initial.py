# Generated by Django 2.0.1 on 2018-01-25 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('street_address', models.TextField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('fluid_ounces', models.DecimalField(decimal_places=2, max_digits=4)),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=4)),
                ('alcohol_by_volume', models.DecimalField(decimal_places=1, max_digits=3)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bars.Bar')),
            ],
        ),
    ]
