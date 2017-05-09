import pyramidcourse.infrastructure.static_cache as static_cache
from pyramidcourse.infrastructure.supressor import suppress
import pyramid.httpexceptions as httpexc
import pyramidcourse.infrastructure.cookie_auth as cookie_auth


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id
        self.page_title = "The Packet Wizard"

    @property
    def is_logged_in(self):
        return True

    # noinspection PyMethodMayBeStatic
    def redirect(self, to_url, permanent=False):
        if permanent:
            raise httpexc.HTTPMovedPermanently(to_url)
        raise httpexc.HTTPFound(to_url)

    @property
    def logged_in_user_id(self):
        return cookie_auth.get_user_id_via_auth_cookie(self.request)
