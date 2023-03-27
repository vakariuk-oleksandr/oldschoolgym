from random import randint
from drf_yasg import openapi


def generate_confirmation_code() -> str:
    return str(randint(100, 999999)).zfill(6)


def get_header_params():
    header_param = openapi.Parameter(
        'Authorization', openapi.IN_HEADER, description="Access token", type=openapi.IN_HEADER)
    return [header_param]


def get_query_params(name: str, description: str = '', type=openapi.TYPE_INTEGER):
    query_param = openapi.Parameter(name, openapi.IN_QUERY,
                                    description=description, type=type)
    return [query_param]


def get_form_params(name: str, description: str = '', type=openapi.TYPE_FILE):
    form_param = openapi.Parameter(
        name, openapi.IN_FORM, description=description, type=type)
    return [form_param]
