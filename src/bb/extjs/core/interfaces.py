from zope.interface import Interface
from zope.interface import Attribute


class IApplicationContext(Interface):
    resource = Attribute('fanstatic resources for all js and css')

