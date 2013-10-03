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
            'block_fields',
            ],
        )

    block_fields = schema.TextLine(
        title=_(u"label_block_fields", default=u"Her tester jeg litt"),
        description=_(u"help_block_fields",
                      default=u"Block some fields")
        )


alsoProvides(IExtraSettings, IMedialogControlpanelSettingsProvider)
