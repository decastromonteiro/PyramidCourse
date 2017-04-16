import pyramidcourse.infrastructure.static_cache as static_cache
from pyramidcourse.infrastructure.supressor import suppress

class BaseController:
    def __init__(self, request, page_title):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id
        self.page_title = page_title


