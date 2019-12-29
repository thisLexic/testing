# Generated by Django 2.2.5 on 2019-12-26 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='form.Branch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='form.Product')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('date', 'product'), ('date', 'branch'), ('branch', 'product')},
            },
        ),
    ]