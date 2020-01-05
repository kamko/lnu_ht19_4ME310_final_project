from flask import jsonify


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

