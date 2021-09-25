from django.shortcuts import get_object_or_404, render
from seoen.models import (BlogCategoryEn, BlogContentEn, BlogPageSeoEn, ContactSeoEn, HomeSeoEn, SliderEn, AboutEn, ApplicationEn,
                          ApplicationCategoryEn, ApplicationSubCategoryEn, QualityEn, KVKKAydınlatmaMetniEn)
from seotr.models import (BlogCategoryTr, BlogContentTr, BlogPageSeoTr, ContactSeoTr, HomeSeoTr, Slider, AboutTr,
                          ReferenceTr, ApplicationTr, ApplicationCategoryTr, ApplicationSubCategoryTr, QualityTr, KVKKAydınlatmaMetniTr)
from django.utils.translation import get_language


def home(request):
    template_name = "home/home.html"
    home_model = HomeSeoEn if get_language() == 'en' else HomeSeoTr
    slider_model = SliderEn if get_language() == 'en' else Slider
    subcategories_model = ApplicationSubCategoryEn if get_language() == 'en' else ApplicationSubCategoryTr
    blog_model = BlogContentEn if get_language() == 'en' else BlogContentTr

    context = {
        'home': home_model.objects.all().first(),
        'sliders': slider_model.objects.all(),
        'applications': subcategories_model.objects.all(),
        'blogs': blog_model.objects.order_by('-created_at')[:3],
    }
    return render(request, template_name, context)


def aboutus(request):
    template_name = "about/about.html"

    about_model = AboutEn if get_language() == 'en' else AboutTr
    reference_model = ReferenceTr
    context = {
        'about': about_model.objects.all().first(),
        'references': reference_model.objects.all(),
    }
    return render(request, template_name, context)


def applications(request):
    template_name = "applications/application.html"
    application_model = ApplicationEn if get_language() == 'en' else ApplicationTr
    subcategories_model = ApplicationSubCategoryEn if get_language(
    ) == 'en' else ApplicationSubCategoryTr

    context = {
        'application': application_model.objects.all().first(),
        'subcategories': subcategories_model.objects.all(),
    }
    return render(request, template_name, context)


def application_category_list(request, slug):
    template_name = "applications/application.html"
    categories_model = ApplicationCategoryEn if get_language(
    ) == 'en' else ApplicationCategoryTr
    subcategories_model = ApplicationSubCategoryEn if get_language(
    ) == 'en' else ApplicationSubCategoryTr
    application_model = ApplicationEn if get_language() == 'en' else ApplicationTr

    category = get_object_or_404(categories_model, slug=slug)

    context = {
        'application': application_model.objects.all().first(),
        'subcategories': subcategories_model.objects.filter(category=category),
        'category': category,
    }
    return render(request, template_name, context)


def application_detail(request, slug):
    template_name = "applications/application_detail.html"
    subcategories_model = ApplicationSubCategoryEn if get_language() == 'en' else ApplicationSubCategoryTr
    application_model = ApplicationEn if get_language() == 'en' else ApplicationTr

    category = get_object_or_404(subcategories_model, slug=slug)
    context = {
        'application': application_model.objects.all().first(),
        'subcategory': category,
        'subcategories': subcategories_model.objects.all(),
    }
    return render(request, template_name, context)


def quality(request):
    template_name = "quality/quality.html"
    quality_model = QualityEn if get_language() == 'en' else QualityTr

    context = {
        'quality': quality_model.objects.all().first(),
    }
    return render(request, template_name, context)


def blog(request):
    template_name = "blog/blog.html"
    blog_model = BlogPageSeoEn if get_language() == 'en' else BlogPageSeoTr
    blogposts_model = BlogContentEn if get_language() == 'en' else BlogContentTr
    blogcategories_model = BlogCategoryEn if get_language() == 'en' else BlogCategoryTr

    context = {
        'blog': blog_model.objects.all().first(),
        'blogposts': blogposts_model.objects.all(),
        'blogcategories': blogcategories_model.objects.all(),
    }
    return render(request, template_name, context)

def blog_category_list(request, slug):
    template_name = "blog/blog.html"

    blog_model = BlogPageSeoEn if get_language() == 'en' else BlogPageSeoTr
    blogposts_model = BlogContentEn if get_language() == 'en' else BlogContentTr
    blogcategories_model = BlogCategoryEn if get_language() == 'en' else BlogCategoryTr

    category = get_object_or_404(blogcategories_model, slug=slug)

    context = {
        'blog': blog_model.objects.all().first(),
        'blogposts': blogposts_model.objects.filter(category=category),
        'blogcategories': blogcategories_model.objects.all(),
        'selectedcategory': category,
    }
    return render(request, template_name, context)

def blog_content(request, slug):
    template_name = "blog/blog_content.html"

    blog_model = BlogPageSeoEn if get_language() == 'en' else BlogPageSeoTr
    blogposts_model = BlogContentEn if get_language() == 'en' else BlogContentTr
    blogcategories_model = BlogCategoryEn if get_language() == 'en' else BlogCategoryTr

    blogpost = get_object_or_404(blogposts_model, slug=slug)

    context = {
        'blog': blog_model.objects.all().first(),
        'latestposts': blogposts_model.objects.order_by('-created_at')[:3],
        'blogcategories': blogcategories_model.objects.all(),
        'blogpost': blogpost,
    }
    return render(request, template_name, context)


def contact(request):
    template_name = "contact/contact.html"

    contact_model = ContactSeoEn if get_language() == 'en' else ContactSeoTr

    context = {
        'contact': contact_model.objects.all().first(),
    }
    return render(request, template_name, context)

def kvkk_page(request):
    template_name = "kvkk.html"

    kvkk_model = KVKKAydınlatmaMetniEn if get_language() == 'en' else KVKKAydınlatmaMetniTr

    context = {
        'kvkk': kvkk_model.objects.all().first(),
    }
    return render(request, template_name, context)
