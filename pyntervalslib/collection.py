# -*- encoding: utf-8 -*-

import urllib

class Collection:
    '''
    TODO: improve that! It is too basic
    TODO: yaml to configure filter?
    '''
    actions = { 'time':['activeonly', 'approved', 'billable', 'clientid', 'date', 'daterange', 'list', 'milestoneid', 'moduleid', 'personid', 'projectid', 'taskid', 'worktypeid' 'sortfield', 'sortdir', 'offset', 'limit']}

    allowed_fields = {
            'time': ["id", "projectid", "moduleid", "taskid", "worktypeid", "personid", "date", "time", "description", "billable", "datemodified", "dateiso", "module", "project", "worktype", "tasklocalid", "task", "firstname", "lastname", "active", "person", "client", "clientactive", "statusid"],
            "person": ["id", "clientid", "title", "firstname", "lastname", "primaryaccount", "notes", "allprojects", "active", "private", "username", "groupid", "group", "client", "numlogins", "lastlogin", "restricttasks"],
            "client": ["id", "name", "datecreated", "description", "website", "phone", "fax", "address", "active"],
            "customer": ["id", "billingid", "subdomain", "firstname", "lastname", "company", "email", "phone", "datesignup", "locale", "message", "plan", "domain", "timezone", "timezone_offset"],
            "group": ["id", "name"],
            "module":["id", "name", "description", "active"],
            "project": ["id", "name", "description", "datestart", "dateend", "alert_percent", "alert_date", "active", "billable", "budget", "clientid", "client", "localid", "manager", "managerid"],
            "task": ["id", "localid", "queueid", "assigneeid", "statusid", "projectid", "moduleid", "title", "summary", "dateopen", "datedue", "dateclosed", "estimate", "ownerid", "priorityid", "color", "priority", "severity", "status", "clientid", "client", "milestoneid", "milestone", "module", "assignees", "followers", "followerid", "owners"],
            "worktype": ["id", "name", "defaulthourlyrate", "active"]
            }

    def __init__(self, action):
        '''
        TODO:  throw exception if not exists
        '''
        self.selected_actions = {}
        if Collection.actions.has_key(action):
            self.action = action

    def add_filter(self, key, value):
        self.selected_actions[key] = value

    def build_query_string(self):
        return urllib.urlencode(self.selected_actions)
