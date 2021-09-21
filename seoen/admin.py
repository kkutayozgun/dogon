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


admin.site.register(MetaKeywordEn)
admin.site.register(HomeSeoEn)
admin.site.register(SliderEn)
admin.site.register(AboutEn)

admin.site.register(ApplicationEn)

class ApplicationCategoryEnAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'banner_image',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(ApplicationCategoryEn, ApplicationCategoryEnAdmin)

class ApplicationSubCategoryEnAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'body', 'cover_image', 'category', 'image', 'pdf_file',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(ApplicationSubCategoryEn, ApplicationSubCategoryEnAdmin)

admin.site.register(QualityEn)

admin.site.register(BlogPageSeoEn)

class BlogCategoryEnAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(BlogCategoryEn, BlogCategoryEnAdmin)

class BlogContentEnAdmin(admin.ModelAdmin):
    fields = ('category','title', 'slug', 'banner_title', 'body', 'image',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(BlogContentEn, BlogContentEnAdmin)

admin.site.register(ContactSeoEn)

admin.site.register(KVKKAydınlatmaMetniEn)