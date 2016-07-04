from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from zope.interface import implements

from cckf.theme.browser.interfaces import ICCKFView

_marker = []


class CCKFView(BrowserView):
    implements(ICCKFView)

    # Utility methods

    def getColumnsClasses(self, view=None):
        """Determine whether a column should be shown. The left column is
        called plone.leftcolumn; the right column is called plone.rightcolumn.
        """

        plone_view = getMultiAdapter(
            (self.context, self.request), name=u'plone')
        portal_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_portal_state')

        sl = plone_view.have_portlets('plone.leftcolumn', view=view);
        sr = plone_view.have_portlets('plone.rightcolumn', view=view);

        isRTL = portal_state.is_rtl()

        # pre-fill dictionary
        columns = dict(one="", content="", two="")

        if not sl and not sr:
            # we don't have columns, thus conten takes the whole width
            columns['content'] = "width-full position-0"

        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            columns['one'] = "width-1:4 position-0"
            columns['content'] = "width-1:2 position-1:4"
            columns['two'] = "width-1:4 position-3:4"

        elif (sr and not sl) and isRTL:
            # We have right column and we are in RTL language
            columns['content'] = "width-3:4 position-1:4"
            columns['two'] = "width-1:4 position-0"

        elif (sr and not sl) and not isRTL:
            # We have right column and we are NOT in RTL language
            columns['content'] = "width-3:4 position-0"
            columns['two'] = "width-1:4 position-3:4"

        elif (sl and not sr) and isRTL:
            # We have left column and we are in RTL language
            columns['one'] = "width-1:4 position-3:4"
            columns['content'] = "width-3:4 position-0"

        elif (sl and not sr) and not isRTL:
            # We have left column and we are in NOT RTL language
            columns['one'] = "width-1:4 position-0"
            columns['content'] = "width-3:4 position-1:4"

        # append cell to each css-string
        for key, value in columns.items():
            columns[key] = "cell " + value

        return columns

    def getColumnsClass(self, view=None):
        """XXX: Keep old customized main_templates working, this should be
           marked as deprecated in future."""

        return self.getColumnsClasses(view).get('content')

    def getNews(self, lang='zh', limit=3):
        """Get Items for FrontPage News
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/cckf/' + lang + '/news'
        return catalog(portal_type='News Item',
                       review_state='published',
                       path=path,
                       sort_on='created',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getActivity(self, lang='zh', limit=3):
        """Get Items for FrontPage Activity
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/cckf/' + lang + '/activities'
        return catalog(portal_type='Event',
                       review_state='published',
                       path=path,
                       sort_on='start',
                       sort_order='descending',
                       sort_limit=limit)[:limit]

    def getSinology(self, lang='zh', classify='01'):
        """Get Items for Sinology HomePage
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        path = '/cckf/' + lang + '/sino'
        return catalog(portal_type='sinology',
                       review_state='published',
                       path=path,
                       classify=classify,
                       sort_on='modified',
                       sort_order='descending',
                       sort_limit=4)[:4]

