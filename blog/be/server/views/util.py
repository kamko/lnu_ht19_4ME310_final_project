from functools import wraps

from flask import jsonify, request

from server.config import AppConfiguration


def jsonify_page(items, page):
    return jsonify({
        'items': items,
        'page': page.page,
        'hasNext': page.has_next,
        'hasPrev': page.has_prev,
        'pages': page.pages,
        'perPage': page.per_page,
        'total': page.total
    })


def admin_api_access(fun):
    @wraps(fun)
    def wrap(*args, **kwargs):
        header = request.headers.get('Authorization')
        if header != f'Bearer {AppConfiguration.ADMIN_ACCESS_TOKEN}':
            return 'not allowed (missing/wrong api token)', 403

        return fun(*args, **kwargs)

    return wrap
