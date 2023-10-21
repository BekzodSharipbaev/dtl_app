from django.views.generic import TemplateView

from .description import TAGS, FILTERS


class HomeView(TemplateView):
    extra_context = {'title': 'Home'}
    template_name = 'dtl_app/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tags'] = TAGS.copy()
        context['filters'] = FILTERS.copy()
        return context
