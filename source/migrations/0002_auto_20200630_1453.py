# Generated by Django 2.2.13 on 2020-06-30 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('cover', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Action and adventure'), (2, 'Art/architecture'), (3, 'Autobiography'), (4, 'Business/economics'), (5, 'Classic'), (6, 'Cookbook'), (7, 'Dictionary'), (8, 'Crime'), (9, 'Encyclopedia'), (10, 'Drama'), (11, 'Guide'), (12, 'Fairytale'), (13, 'Health/fitness'), (14, 'Fantasy'), (15, 'History'), (16, 'Humor'), (17, 'Horror'), (18, 'Journal'), (19, 'Mystery')], default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='postal',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='town',
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
