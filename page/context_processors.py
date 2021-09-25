from seoen.models import (ApplicationCategoryEn)
from seotr.models import (ApplicationCategoryTr)
from django.utils.translation import get_language
from django.conf import settings


def categories_processor(request):
    categories_model = ApplicationCategoryEn if get_language() == 'en' else ApplicationCategoryTr    
    categories = categories_model.objects.all()
    return {'appcategories': categories}

def googleapikey_processor(request):
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}
