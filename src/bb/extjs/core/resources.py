import fanstatic

from grokcore import component
from zope.interface import implementer

from js.extjs import basic

from bb.extjs.core.interfaces import IApplicationContext
from bb.extjs.resources.interfaces import IClassPathMapping





@implementer(IClassPathMapping)
class BaseClassPathMapping(component.Subscription):
    """ Base class for all extjs class path mapping registrations
    """
    component.baseclass()
    component.context(IApplicationContext)
    namespace=''
    path=''


class ExtClassPathMapping(BaseClassPathMapping):
    namespace='Ext'
    path='fanstatic/extjs/src/'


class BootstrapFanstaticResource(fanstatic.Resource):

    def __init__(self):
        
        old_state = fanstatic.core._resource_file_existence_checking
        fanstatic.core._resource_file_existence_checking = False
        super(BootstrapFanstaticResource, self).__init__(fanstatic.Library('', ''), 'fake.js', depends=[basic])
        fanstatic.core._resource_file_existence_checking = old_state

    def render(self, library_url):
        baseurl = library_url.rsplit('/', 2)[0]
        return self.renderer('%s/bootstrap' % baseurl)

extjs_resources = BootstrapFanstaticResource()
