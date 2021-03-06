# Generated by Django 3.1.1 on 2020-09-11 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mutter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日')),
            ],
            options={
                'verbose_name': 'Mutter',
            },
        ),
    ]
