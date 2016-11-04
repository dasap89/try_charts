from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DataModel
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
class ChartView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(ChartView, self).get_context_data(**kwargs)
        context['data'] = DataModel.objects.all()
        return context
    
def chart_data(request):
    
    data_for_chart = DataModel.objects.all()

    data = serializers.serialize('json', data_for_chart)

    return HttpResponse(data, content_type='application/json')
