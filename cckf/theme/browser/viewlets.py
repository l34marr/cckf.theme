from zope.i18n import translate
from plone.app.layout.viewlets.common import TitleViewlet


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

