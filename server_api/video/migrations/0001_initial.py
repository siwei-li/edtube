# Generated by Django 3.1.4 on 2021-03-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('YT', 'youtube'), ('KA', 'khanacademy')], default='YT', max_length=2)),
                ('platform_id', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('description', models.TextField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('category_id', models.IntegerField()),
            ],
            options={
                'db_table': 'videos',
            },
        ),
    ]