from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # This one's broken because of the issue
    config.add_route('broken', '/broken')

    # These ones work
    config.add_route('works', '/works')
    config.add_route('works2', '/works2')

    config.scan()

    # Jinja config:
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_jinja2_search_path('pyramid_jinja_issue:templates', name='.html')

    return config.make_wsgi_app()
