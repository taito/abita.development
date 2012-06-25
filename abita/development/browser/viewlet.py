from Products.ATContentTypes.interfaces.folder import IATFolder
from abita.development.browser.interfaces import IAbitaDevelopmentLayer
from abita.development.interfaces import IManageDevWork
from abita.development.interfaces import IRate
from five import grok
from plone.app.layout.globals.interfaces import IViewView
from plone.app.layout.viewlets.interfaces import IAboveContentTitle
from zope.annotation.interfaces import IAnnotations


grok.templatedir('viewlets')


class RatePerTenMinutesViewlet(grok.Viewlet):
    """Rate per ten minutes Viewlet Class."""
    grok.context(IATFolder)
    grok.layer(IAbitaDevelopmentLayer)
    grok.name('rate-per-ten-minutes')
    grok.require('cmf.ManagePortal')
    grok.template('rate')
    grok.view(IViewView)
    grok.viewletmanager(IAboveContentTitle)

    def update(self):
        form = self.request.form
        if form.get('form.button.Update', None) is not None:
            try:
                rate = float(form.get('rate', ''))
                IAnnotations(self.context)['abita.development.rate'] = rate
                return self.render()
            except ValueError:
                pass

    def available(self):
        """Return True if the context provides IManageDevWork interface."""
        return IManageDevWork.providedBy(self.context)

    def rate(self):
        return IRate(self.context)()
