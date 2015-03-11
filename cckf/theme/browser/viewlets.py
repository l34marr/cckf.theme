from zope.i18n import translate
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import TitleViewlet
from plone.app.layout.links.viewlets import FaviconViewlet


class TitleViewlet(TitleViewlet):
    """Custom Title
    """
    def update(self):
        super(TitleViewlet, self).update()
        self.site_title = u"%s &mdash; %s" % (self.page_title,
            translate('portal_title',
                      domain='plone',
                      context=self.request,
                      default='CCKF'))


class FaviconViewlet(FaviconViewlet):
    """Custom Favicon
    """
    _template = ViewPageTemplateFile('favicon.pt')

