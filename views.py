from django.http import HttpResponse
from django.template import loader

def show_map(request):
    template = loader.get_template('map.html')
    context = {}
    renderer_page = template.render(context, request)
    return HttpResponse(renderer_page)