from .admin import blueprint as admin
from .article import blueprint as article
from .root import blueprint as root

__all__ = [
    'root',
    'admin',
    'article'
]
