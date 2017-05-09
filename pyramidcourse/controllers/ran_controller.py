from pyramidcourse.controllers.base_controller import BaseController
from pyramidcourse.services.ran_services import RANService
import pyramid_handlers


class RanController(BaseController):
    @pyramid_handlers.action(renderer='/templates/ran/index.jinja2')
    def index(self):
        routing_area_code = RANService.get_routing_area_code()
        return {

            'ran_nodes': routing_area_code

        }
