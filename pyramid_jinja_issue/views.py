from pyramid.renderers import render
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='broken', renderer='email/mytemplate.html')
@view_config(route_name='works', renderer='mytemplate.html')
def my_view(request):
    return {"name": "Bruce"}
