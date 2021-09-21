from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.

class MetaKeywordEn(models.Model):
    keyword = models.CharField(_('Anahtar Kelime'), max_length=100)

    class Meta:
        verbose_name = _('EN Anahtar Kelime')
        verbose_name_plural = _('EN Anahtar Kelimeler')

    def __str__(self):
        return self.keyword

class SeoAbstractModel(models.Model):
    seo_title = models.CharField(_('SEO Başlığı:'), max_length=200, blank=True, null=True)
    meta_description = models.TextField(_('Meta Açıklaması:'), blank=True, null=True)
    meta_keywords = models.ManyToManyField(MetaKeywordEn, verbose_name=_('Anahtar Kelimeler'))

    class Meta:
        abstract = True

class HomeSeoEn(SeoAbstractModel):

    class Meta:
        verbose_name = _('EN SEO Anasayfa')
        verbose_name_plural = _('EN SEO Anasayfa')

    def __str__(self):
        return self.seo_title

class SliderEn(models.Model):
    title_layer1 = models.CharField(_('Slider Başlığı (1.Satır):'), max_length=100)
    title_layer2 = models.CharField(_('Slider Başlığı (2.Satır):'), max_length=100, blank=True, null=True)
    body = models.TextField(_('Slider İçeriği:'), blank=True, null=True)
    button_url = models.CharField(_('SSlider Yönlendirme Linki:'), max_length=300)
    sliderimage = models.ImageField(verbose_name=_('Slider Görseli:'), upload_to='slider')

    class Meta:
        verbose_name = _('EN Slider İçeriği')
        verbose_name_plural = _('EN Slider İçerikleri')
    
    def __str__(self):
        return f"{self.title_layer1} {self.title_layer2}"


class AboutEn(SeoAbstractModel):
    banner = models.CharField(_('Banner Başlık:'), max_length=200)
    banner_image = models.ImageField(verbose_name=_('Banner Görseli:'), upload_to="about")
    
    title1 = models.CharField(_('Açıklama Başlığı'), max_length=200)
    body1 = RichTextField(verbose_name=_('Açıklama İçeriği:'), blank=True, null=True)
    image1 = models.ImageField(verbose_name=_('Açıklama Görseli:'), upload_to="about")

    title2 = models.CharField(_('Alt Açıklama Başlığı:'), max_length=200)
    body2 = RichTextField(verbose_name=_('Alt Açıklama İçeriği:'), blank=True, null=True)
    image2 = models.ImageField(verbose_name=_('Alt Açıklama Görseli:'), upload_to="about")

    class Meta:
        verbose_name = _('EN Hakkımızda Sayfası')
        verbose_name_plural = _('EN Hakkımızda Sayfası')

    def __str__(self):
        return self.banner


class ApplicationEn(SeoAbstractModel):
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    banner_image = models.ImageField(_('Banner Resmi:'), upload_to='applications/banner')

    class Meta:
        verbose_name = _('TR Uygulamalar SEO')
        verbose_name_plural = _('TR Uygulamalar SEO')

    def __str__(self):
        return self.banner_title


class ApplicationCategoryEn(SeoAbstractModel):
    title = models.CharField(_('Başlık:'), max_length=200)
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    banner_image = models.ImageField(_('Banner Resim:'), upload_to="applications/category")

    slug = models.SlugField(_('URL Uzantısı:'), max_length=200)

    class Meta:
        verbose_name = _('TR Uygulama Kategori')
        verbose_name_plural = _('TR Uygulama Kategorileri')

    def __str__(self):
        return self.title

class ApplicationSubCategoryEn(SeoAbstractModel):
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)

    title = models.CharField(_('Başlık:'), max_length=200)
    body = RichTextField(verbose_name=_('Açıklama:'), blank=True, null=True)
    cover_image = models.ImageField(verbose_name=_('Kapak Resmi:'), upload_to="applications/items/", blank=True, null=True)

    category = models.ForeignKey(ApplicationCategoryEn, on_delete=models.CASCADE, blank=True, null=True)

    slug = models.SlugField(_('URL Uzantısı:'), max_length=200)
    image = models.ImageField(verbose_name=_('İçerik Resmi:'), upload_to="applications/items/", blank=True, null=True)

    pdf_file = models.FileField(_('Broşür Dosyası'), upload_to="applications/pdf", blank=True, null=True)

    class Meta:
        verbose_name = _('EN Uygulama Alt Kategorisi')
        verbose_name_plural = _('EN Uygulama Alt Kategorileri')

    def __str__(self):
        return self.title

    
class QualityEn(SeoAbstractModel):
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    
    title = models.CharField(_('İçerik Başlığı'), max_length=200)
    body = RichTextField(verbose_name=_('Kalite İçeriği:'), blank=True, null=True)
    banner_image = models.ImageField(verbose_name=_('Banner Resmi:'), upload_to="quality")

    image = models.ImageField(verbose_name=_('İçerik Resmi:'), upload_to="quality")

    class Meta:
        verbose_name = _('EN Kalite Sayfası')
        verbose_name_plural = _('EN Kalite Sayfası')

    def __str__(self):
        return self.title


class BlogPageSeoEn(SeoAbstractModel):
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    banner_image = models.ImageField(verbose_name=_('Banner Görseli:'), upload_to="blog")

    class Meta:
        verbose_name = _('EN Blog Sayfası SEO')
        verbose_name_plural = _('EN Blog Sayfası SEO')

    def __str__(self):
        return self.banner_title


class BlogCategoryEn(SeoAbstractModel):
    title = models.CharField(_('Blog Kategori:'), max_length=200)
    slug = models.SlugField(_('URL Uzantısı:'), max_length=200, db_index=True)

    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)

    class Meta:
        verbose_name = _('EN Blog Kategori')
        verbose_name_plural = _('EN Blog Kategoriler')

    def __str__(self):
        return self.title

class BlogContentEn(SeoAbstractModel):
    category = models.ForeignKey(BlogCategoryEn, verbose_name=_('Blog Kategori'), on_delete=models.CASCADE)
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    title = models.CharField(_('İçerik Başlık:'), max_length=200)
    slug = models.SlugField(_('URL Uzantısı:'), max_length=200, db_index=True)
    
    body = RichTextField(verbose_name=_('Blog İçeriği:'), blank=True, null=True)
    image = models.ImageField(verbose_name=_('Blog Görseli:'), upload_to="blog")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Eklenme Zamanı'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Güncellenme Zamanı'))
    
    class Meta:
        verbose_name = _('TR Blog İçerik')
        verbose_name_plural = _('TR Blog İçerikleri')

    def __str__(self):
        return self.title


class ContactSeoEn(SeoAbstractModel):
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    banner_image = models.ImageField(verbose_name=_('Banner Görseli:'), upload_to="contact")

    class Meta:
        verbose_name = _('EN İletişim Sayfası')
        verbose_name_plural = _('EN İletişim Sayfası')

    def __str__(self):
        return self.banner_title


class KVKKAydınlatmaMetniEn(SeoAbstractModel):
    banner_title = models.CharField(_('Banner Başlık:'), max_length=200)
    banner_image = models.ImageField(verbose_name=_('Banner Görseli:'), upload_to="contact")

    body = RichTextField(verbose_name=_('KVKK Metni'))

    class Meta:
        verbose_name = _('EN KVKK Aydınlatma Metni')
        verbose_name_plural = _('EN KVKK Aydınlatma Metni')

    def __str__(self):
        return self.banner_title