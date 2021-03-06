# Generated by Django 2.2.4 on 2019-08-02 03:32

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='标题')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='url标识符')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('num_views', models.IntegerField(default=0, verbose_name='浏览数量')),
                ('num_favorites', models.IntegerField(default=0, verbose_name='收藏数量')),
                ('show_status', models.BooleanField(default=True, verbose_name='显示状态')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='类别名称')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='url标识符')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '节点类别',
                'verbose_name_plural': '节点分类列表',
            },
        ),
        migrations.CreateModel(
            name='FriendsURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=50, unique=True, verbose_name='用户名称')),
                ('friend_image', models.ImageField(max_length=41943040, upload_to='friends', verbose_name='用户头像')),
                ('site_name', models.CharField(max_length=50, unique=True, verbose_name='网站名称')),
                ('site_link', models.URLField(blank=True, max_length=256, null=True, verbose_name='网站链接')),
                ('show_status', models.BooleanField(default=True, verbose_name='显示状态')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接列表',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='原创', max_length=128, unique=True, verbose_name='站点名称')),
                ('url', models.URLField(blank=True, max_length=128, null=True, verbose_name='url')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '文章来源',
                'verbose_name_plural': '文章来源列表',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='标签')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='url标识符')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签列表',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='节点名称')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='url标识符')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('num_topics', models.IntegerField(default=0, verbose_name='主题数量')),
                ('show_status', models.BooleanField(default=True, verbose_name='显示状态')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Category', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '节点',
                'verbose_name_plural': '节点列表',
            },
        ),
    ]
