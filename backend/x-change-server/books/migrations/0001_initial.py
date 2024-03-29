# Generated by Django 2.2.2 on 2019-06-14 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
                ('thumb', models.ImageField(blank=True, upload_to='covers/')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('isbn', models.CharField(max_length=17, null=True, verbose_name='ISBN')),
                ('description', models.TextField(help_text='Enter         a brief description of the book', max_length=1000, null=True)),
                ('status', models.CharField(choices=[('AV', 'available'), ('OL', 'on loan'), ('RQ', 'requested'), ('NA', 'not available')], default='AV', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='RQ', max_length=2)),
                ('date_requested', models.DateTimeField(blank=True, null=True)),
                ('date_borrowed', models.DateTimeField(blank=True, null=True)),
                ('date_returned', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
