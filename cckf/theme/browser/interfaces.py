from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from zope.viewlet.interfaces import IViewletManager


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """

class ICCKFView(Interface):
    """ """

    def getColumnsClass():
        """Returns the CSS class for column content based on columns presence.
        """

    def getColumnsClasses():
        """Returns all CSS classes based on columns presence.
        """

    def getNews():
        """Returns Specific Items for Template.
        """

    def getSinology():
        """Returns Specific Items for Template.
        """

class ICustomNavigation(IViewletManager):
    """Custom Viewlet Manager for Navigation.
    """

