# Generated by Django 2.1.7 on 2019-02-24 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posttitle', models.CharField(max_length=100)),
                ('posttext', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Userblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('userinfo', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='userb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Userblog'),
        ),
    ]