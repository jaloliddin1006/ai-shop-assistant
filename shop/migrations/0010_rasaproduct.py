# Generated by Django 5.1.4 on 2024-12-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='RasaProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('child', 'Child')], max_length=10)),
                ('stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('atr_id', models.PositiveIntegerField()),
                ('ctg_id', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]
