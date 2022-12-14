# Generated by Django 3.2.14 on 2022-10-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('', '---------'), ('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('category', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, choices=[('', '---------'), ('Mass', 'Mass'), ('Celebration', 'Celebration')], max_length=15, null=True)),
                ('image_400_by_400', models.ImageField(blank=True, null=True, upload_to='')),
                ('event_start_date', models.DateTimeField(blank=True, null=True)),
                ('event_end_date', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('snippet', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
                'ordering': ['-event_start_date'],
            },
        ),
    ]
