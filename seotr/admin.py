from django.contrib import admin
from seotr.models import (
    BlogCategoryTr,
    BlogContentTr,
    BlogPageSeoTr,
    ContactSeoTr,
    KeywordsTr,
    HomeSeoTr,
    Slider,
    AboutTr,
    ReferenceTr,
    ApplicationTr,
    ApplicationCategoryTr,
    ApplicationSubCategoryTr,
    QualityTr,
    KVKKAydınlatmaMetniTr
)


SEO_FIELDS = ('seo_title', 'meta_description', 'meta_keywords')

admin.site.register(KeywordsTr)


@admin.register(HomeSeoTr)
class HomeSeoTrAdmin(admin.ModelAdmin):
    fields = SEO_FIELDS


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    fields = ('title_layer1', 'title_layer2',
              'body', 'button_url', 'sliderimage')


@admin.register(AboutTr)
class AboutTrAdmin(admin.ModelAdmin):
    fields = ('banner', 'banner_image', 'title1', 'body1',
              'image1', 'title2', 'body2', 'image2') + SEO_FIELDS


admin.site.register(ReferenceTr)


@admin.register(ApplicationTr)
class ApplicationTrAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image') + SEO_FIELDS


@admin.register(ApplicationCategoryTr)
class ApplicationCategoryTrAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'banner_image') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(ApplicationSubCategoryTr)
class ApplicationSubCategoryTrAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'body', 'cover_image',
              'category', 'image', 'pdf_file') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(QualityTr)
class QualityTrAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image',
              'title', 'body', 'image') + SEO_FIELDS


@admin.register(BlogPageSeoTr)
class BlogPageSeoTrAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image') + SEO_FIELDS


@admin.register(BlogCategoryTr)
class BlogCategoryTrAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(BlogContentTr)
class BlogContentTrAdmin(admin.ModelAdmin):
    fields = ('category', 'banner_title', 'title',
              'slug', 'body', 'image') + SEO_FIELDS
    prepopulated_fields = {'slug': ('title',), }


@admin.register(ContactSeoTr)
class ContactSeoTrAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image') + SEO_FIELDS


@admin.register(KVKKAydınlatmaMetniTr)
class KVKKAydınlatmaMetniTrAdmin(admin.ModelAdmin):
    fields = ('banner_title', 'banner_image', 'body') + SEO_FIELDS
