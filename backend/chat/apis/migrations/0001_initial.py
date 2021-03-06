# Generated by Django 2.0.1 on 2018-02-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='用户名')),
                ('msg', models.TextField(verbose_name='聊天消息')),
                ('gentime', models.DateTimeField(verbose_name='消息生成时间')),
            ],
        ),
    ]
