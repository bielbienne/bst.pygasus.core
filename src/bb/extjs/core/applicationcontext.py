from martian import baseclass
from zope.interface import implementer
from bb.extjs.core.interfaces import IApplicationContext
from grokcore.component import GlobalUtility


@implementer(IApplicationContext)
class ApplicationContext(GlobalUtility):
    """ Represent a ExtJs Application. This is abstract
        class and need to subclass in your project.
    """
    
    baseclass()
