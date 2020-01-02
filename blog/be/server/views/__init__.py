from .root import blueprint as root
from .admin import blueprint as admin
from .article import blueprint as article

__all__ = [
    'root',
    'admin',
    'article'
]
