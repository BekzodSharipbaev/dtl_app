from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def render_txt(context, txt: str, *args, **kwargs):
    tpl = template.Template(txt)
    return tpl.render(context)
