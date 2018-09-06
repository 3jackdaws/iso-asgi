
from jinja2 import Environment, FileSystemLoader, select_autoescape
from quart import Response

template_env = Environment(
    loader=FileSystemLoader('iso/templates'),
    autoescape=select_autoescape(['html']),
    enable_async=True
)


async def render(template, context=None):
    if context is None:
        context = {}
    template = template_env.get_template(template)
    rendered_template = await template.render_async(**context)
    return Response(rendered_template, content_type='text/html')