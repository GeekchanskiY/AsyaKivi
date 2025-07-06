import django.http.request

from .models import Session


def process_user_visit(request: django.http.request.HttpRequest):
    try:
        session = Session.objects.get(session_key=request.session.session_key)
    except Session.DoesNotExist:
        user_ip, user_agent = get_user_data(request)
        session = Session.objects.create(session_key=request.session.session_key, ip=user_ip, user_agent=user_agent)

    print(session)

def get_user_data(request: django.http.request.HttpRequest) -> (str, str):
    """
    get user data - return user_agent and ip from request

    Args:
        request (django.http.request.HttpRequest)

    Returns:
        (str, str): user_agent, ip
    """

    user_agent = request.META.get('HTTP_USER_AGENT')
    ip = request.META.get('REMOTE_ADDR')

    return user_agent, ip