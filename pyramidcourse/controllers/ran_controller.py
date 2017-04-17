from pyramidcourse.controllers.base_controller import BaseController
from pyramidcourse.services.ran_services import RanService
import pyramid_handlers


class RanController(BaseController):
    @pyramid_handlers.action(renderer='/templates/ran/index.jinja2')
    def index(self):
        ran_nodes = RanService.get_ran_nodes()
        return {

            'ran_nodes': ran_nodes

        }
