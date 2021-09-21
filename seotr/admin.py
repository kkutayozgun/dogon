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


admin.site.register(KeywordsTr)
admin.site.register(HomeSeoTr)
admin.site.register(Slider)
admin.site.register(AboutTr)
admin.site.register(ReferenceTr)
admin.site.register(ApplicationTr)


class ApplicationCategoryTrAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'banner_image',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(ApplicationCategoryTr, ApplicationCategoryTrAdmin)

class ApplicationSubCategoryTrAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title', 'body', 'cover_image', 'category', 'image', 'pdf_file',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(ApplicationSubCategoryTr, ApplicationSubCategoryTrAdmin)


admin.site.register(QualityTr)

admin.site.register(BlogPageSeoTr)

class BlogCategoryTrAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'banner_title',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(BlogCategoryTr, BlogCategoryTrAdmin)

class BlogContentTrAdmin(admin.ModelAdmin):
    fields = ('category','title', 'slug', 'banner_title', 'body', 'image',
              'seo_title', 'meta_description', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(BlogContentTr, BlogContentTrAdmin)

admin.site.register(ContactSeoTr)

admin.site.register(KVKKAydınlatmaMetniTr)
