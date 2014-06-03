import fanstatic
from js.extjs import basic


class BootstrapFanstaticResource(fanstatic.Resource):
    def __init__(self):
        
        old_state = fanstatic.core._resource_file_existence_checking
        fanstatic.core._resource_file_existence_checking = False
        super(BootstrapFanstaticResource, self).__init__(fanstatic.Library('', ''), 'fake.js', depends=[basic])
        fanstatic.core._resource_file_existence_checking = old_state

    def render(self, library_url):
        return self.renderer('bootstrap')

extjs_resources = BootstrapFanstaticResource()