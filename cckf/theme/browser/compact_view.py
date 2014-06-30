from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

# from Products.CMFCore.utils import getToolByName


class CompactView(BrowserView):

    template = ViewPageTemplateFile('compact_view.pt')

    def getContent(self,
                   container=None,
                   videos=0,
                   folders=0,
                   others=0):
        """ Mostly ripped out from atctListAlbum.py
        """

        if not container:
            container = self.context

        result = {}

        if videos:
            result['videos'] = container.getFolderContents(
                {'portal_type': ('Document',)}, full_objects=True)

        if folders:
            result['folders'] = container.getFolderContents(
                {'portal_type': ('Folder',)})

        if others:
            utils = getToolByName(self.context, 'plone_utils')
            searchContentTypes = utils.getUserFriendlyTypes()
            filtered = [p_type for p_type in searchContentTypes
                        if p_type not in ('Document', 'Folder',)]
            if filtered:
                # We don't need the full objects for the folder_listing
                result['others'] = container.getFolderContents(
                    {'portal_type': filtered})
            else:
                result['others'] = ()

        return result
