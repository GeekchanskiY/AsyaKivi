from django.shortcuts import render
from .utils import get_user_data, process_user_visit

def index(request):
    """View function for home page of site."""

    if not request.session.session_key:
        request.session.create()

    print(request.session.session_key)
    print(get_user_data(request))

    print(process_user_visit(request))

    return render(request, 'index.html', context=None)