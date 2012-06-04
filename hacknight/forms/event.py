# -*- coding: utf-8 -*-

import flask.ext.wtf as wtf
from baseframe.forms import Form, RichTextField
from pytz import all_timezones
#from baseframe.staticdata import timezones

__all__ = ['EventForm']

timezone_list = [(tz, tz) for tz in all_timezones]
class ValidateEvent(object):
    @staticmethod
    def date(form, field):
        if form.start_datetime.data >= field.data:
            raise wtf.ValidationError('End Date must be greater than Start Date')
        """Need to check if the datetime is past date time, obstacle is Need to have time zone detail, check accordingly.
        """
class EventForm(Form):
    title = wtf.TextField("Title", description="Name of the Event", validators=[wtf.Required()])
    description = RichTextField("Description", description="Description of the project")
    #need to datepicker here, for time being while python datetime module is used inside views
    event_timezone = wtf.SelectField(u"Event Time Zone", choices=timezone_list, default="Asia/Kolkatta") 
    start_datetime = wtf.DateTimeField("StartDateTime", description="Hacknight Start DateTime", validators=[wtf.Required()])
    end_datetime = wtf.DateTimeField("EndDateTime", description="Hacknight End DateTime", validators=[wtf.Required(), ValidateEvent.date])
    website = wtf.TextField("Website",description="Main Event Website", validators=[wtf.Optional()])