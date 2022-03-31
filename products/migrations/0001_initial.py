# Generated by Django 2.2 on 2022-03-30 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('sku', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]
