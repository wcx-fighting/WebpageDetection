# Generated by Django 3.2.2 on 2021-07-07 08:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('createtime', models.DateTimeField(default=datetime.datetime(2021, 7, 7, 16, 42, 55, 715933), verbose_name='用户创建时间')),
                ('judge', models.BooleanField(default=True, verbose_name='判断用户状态')),
            ],
            options={
                'verbose_name': '用户列表',
                'verbose_name_plural': '用户列表',
            },
        ),
        migrations.CreateModel(
            name='RiskUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domainname', models.CharField(max_length=200, verbose_name='域名')),
                ('url', models.CharField(max_length=100, verbose_name='危险URL')),
                ('type', models.IntegerField(max_length=2, verbose_name='危险类型')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebMonitoring.user')),
            ],
            options={
                'verbose_name': '安全事件',
                'verbose_name_plural': '安全事件',
            },
        ),
        migrations.CreateModel(
            name='DetictionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='网址')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebMonitoring.user')),
            ],
            options={
                'verbose_name': '网址列表',
                'verbose_name_plural': '网址列表',
            },
        ),
    ]
