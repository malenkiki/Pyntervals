# -*- encoding: utf-8 -*-

import urllib

class Collection:
    '''
    TODO: improve that! It is too basic
    TODO: yaml to configure filter?
    '''
    actions = { 'time':['activeonly', 'approved', 'billable', 'clientid', 'date', 'daterange', 'list', 'milestoneid', 'moduleid', 'personid', 'projectid', 'taskid', 'worktypeid' 'sortfield', 'sortdir', 'offset', 'limit']}


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
