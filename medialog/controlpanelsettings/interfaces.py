from z3c.form import interfaces

from zope import schema
#from zope.interface import Interface
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.controlpanelsettings')


                                  
class IExtraSettings(form.Schema):
    """Adds settings to medialog.controlpanel
    """

    form.fieldset(
        'extra',
        label=_(u'Extra Settings'),
        fields=[
            'extra_field',
            ],
        )

    extra_field = schema.TextLine(
        title=_(u"label_extra_field", default=u"Showing off"),
        description=_(u"help_extra_field",
                      default=u"Some text here")
        )


alsoProvides(IExtraSettings, IMedialogControlpanelSettingsProvider)
