from django.contrib import admin
from seoen.models import (
    BlogCategoryEn,
    BlogContentEn,
    BlogPageSeoEn,
    ContactSeoEn,
    MetaKeywordEn,
    HomeSeoEn,
    SliderEn,
    AboutEn,
    ApplicationEn,
    ApplicationCategoryEn,
    ApplicationSubCategoryEn,
    QualityEn,
    KVKKAydınlatmaMetniEn,
)


SEO_FIELDS = ('seo_title', 'meta_description', 'meta_keywords')

admin.site.register(MetaKeywordEn)


@admin.register(HomeSeoEn)
class HomeSeoEnAdmin(admin.ModelAdmin):
    fields = SEO_FIELDS


@admin.register(SliderEn)
class SliderEnAdmin(admin.ModelAdmin):
    fields = ('title_layer1', 'title_layer2',
              'body', 'button_url', 'sliderimage')


@admin.register(AboutEn)
class AboutEnAdmin(admin.ModelAdmin):
    fields = ('banner', 'banner_image', 'title1', 'body1',
              'image1', 'title2', 'body2', 'image2') + SEO_FIELDS


@admin.register(ApplicationEn)
class ApplicationEnAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image') + SEO_FIELDS


@admin.register(ApplicationCategoryEn)
class ApplicationCategoryEnAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'banner_image') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(ApplicationSubCategoryEn)
class ApplicationSubCategoryEnAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'body', 'cover_image',
              'category', 'image', 'pdf_file') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(QualityEn)
class QualityEnAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image',
              'title', 'body', 'image') + SEO_FIELDS


@admin.register(BlogPageSeoEn)
class BlogPageSeoEnAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image') + SEO_FIELDS


@admin.register(BlogCategoryEn)
class BlogCategoryEnAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(BlogContentEn)
class BlogContentEnAdmin(admin.ModelAdmin):
    fields = ('category', 'banner_title', 'title',
              'slug', 'body', 'image') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(ContactSeoEn)
class ContactSeoEnAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image') + SEO_FIELDS


@admin.register(KVKKAydınlatmaMetniEn)
class KVKKAydınlatmaMetniEnAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image', 'body') + SEO_FIELDS
