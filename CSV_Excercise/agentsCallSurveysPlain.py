import os, sys, datetime, pytz, math, csv

paths = (str(os.getcwd()),
    str(os.getcwd())+'\\wix\\',
    str(os.getcwd())+'\\wix\\models\\',
    str(os.getcwd())+'\\contactual\\')

for path in paths:
    if path not in sys.path: sys.path.append(path)

from django.core.management import setup_environ
import settings as import_settings
setup_environ(import_settings)

import wix, wix.models, contactual.models
from django.db import models

timezone = pytz.timezone('US/Pacific')

w = csv.writer(open('Source.csv', 'wb'))

w.writerow(["call_id", "Call Direction", "call date/time", "user_id", "agent_id", "agent_name", "Survey Gizmo ID", "submitted date/time", "submitted date", "serv_sat", "wix_sat",
            "rep_prompt", "rep_curt", "rep_help", "rep_know", "rep_effic", "rep_needs"])


startDate = datetime.datetime.now(pytz.utc).replace(tzinfo=None) - datetime.timedelta(days=30)
#surveys = wix.models.CallSurvey.objects.filter(submitted__gte=startDate).all()
surveys = wix.models.CallSurvey.objects.all()

#endDate = datetime.datetime(2013,4,15,0,0).replace(tzinfo=None)
#startDate = endDate - datetime.timedelta(days=30)
#surveys = wix.models.CallSurvey.objects.filter(submitted__gte=startDate).filter(submitted__lte=endDate).all()
for survey in surveys:

    try:    userGUID = survey.user.guid
    except: userGUID = None
    
    try:
        tmp = survey.submitted.replace(tzinfo=pytz.utc).astimezone(timezone).replace(tzinfo=None)
        submitDate = tmp.strftime("%m/%d/%y")
        submitDateTime = tmp.strftime('%m/%d/%Y %H:%M')
        callStart = survey.call.start.strftime('%m/%d/%Y %H:%M')
    except: callStart = submitDate = submitDateTime = None
    
    if survey.call.agent:
        w.writerow([survey.call_id, survey.call.type, callStart, survey.user_id, survey.call.agent_id, survey.call.agent.first_name+' '+survey.call.agent.last_name,
                    survey.ext_sys_id, submitDateTime, submitDate, survey.serv_sat, survey.wix_sat,
                    survey.rep_prompt, survey.rep_curt, survey.rep_help, survey.rep_know, survey.rep_effic, survey.rep_needs])
