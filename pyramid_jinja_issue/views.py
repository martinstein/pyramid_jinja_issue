from pyramid.view import view_config


@view_config(route_name='broken', renderer='email/other_template.html')
@view_config(route_name='works2', renderer='pyramid_jinja_issue:templates/email/other_template.html')
@view_config(route_name='works', renderer='some_template.html')
def my_view(request):
    return {"name": "Bruce"}
