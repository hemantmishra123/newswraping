# Generated by Django 3.1.1 on 2020-09-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todoitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('data1', models.IntegerField()),
                ('data2', models.IntegerField()),
                ('data3', models.IntegerField()),
                ('data4', models.IntegerField()),
                ('data5', models.IntegerField()),
            ],
        ),
    ]