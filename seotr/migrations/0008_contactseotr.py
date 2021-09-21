# Generated by Django 2.2 on 2021-09-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seotr', '0007_auto_20210919_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSeoTr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Başlığı:')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Açıklaması:')),
                ('banner_title', models.CharField(max_length=200, verbose_name='Banner Başlık:')),
                ('banner_image', models.ImageField(upload_to='contact', verbose_name='Banner Görseli:')),
                ('meta_keywords', models.ManyToManyField(to='seotr.KeywordsTr', verbose_name='Anahtar Kelimeler')),
            ],
            options={
                'verbose_name': 'TR İletişim Sayfası',
                'verbose_name_plural': 'TR İletişim Sayfası',
            },
        ),
    ]
