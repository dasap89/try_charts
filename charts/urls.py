from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import ChartView, chart_data


urlpatterns = [
	url(r'^$', ChartView.as_view(), name='data'),
	url(r'get_data/$', chart_data, name='get_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
