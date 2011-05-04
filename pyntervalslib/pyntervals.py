# -*- encoding: utf-8 -*-

import urllib2
import base64
import json
#import time
#import re
#import httplib2

class Pyntervals:
    '''
    Todo: have un config ini file for token as alternate touse param to get it
    '''
    actions_allowed = [
            'client', 
            'contactdescriptor', 
            'contacttype',
            'customer',
            'document',
            'group',
            'me', 
            'milestone', 
            'milestonenote',
            'module',
            'person',
            'personcontact', 
            'project',
            'projectmodule',
            'projectnote',
            'projectworktype', 
            'request', 
            'settings',
            'task', 
            'tasklistfilter', 
            'tasknote', 
            'taskpriority', 
            'taskstatus', 
            'time',
            'timer',
            'worktype'
            ]
    actions_only_one = ['me']

    def __init__(self, token):
        '''
        Constructor must have token string… because without it, we do nothing.
        '''
        self.token    = token
        self.password = 'X'
        self.top_url  = 'https://api.myintervals.com/'
        self.use_python() # by default
        self.group = self.get_action('me')[u'group']
        self.errors = []


    def use_python(self):
        self.use_json()
        self.python = True

    def login(self):
        base64_string = base64.encodestring('%s:%s' % (self.token, self.password))[:-1]
        self.request.add_header("Authorization", "Basic %s" % base64_string)

    def use_json(self):
        self.json   = True
        self.xml    = False
        self.python = False

    def use_xml(self):
        self.json   = False
        self.xml    = True
        self.python = False

    def export_format(self):
        export_string = 'json'

        if self.xml:
            export_string = 'xml'
        
        return export_string

    def set_accept_json_or_xml(self):
        header_string = 'json'

        if self.xml:
            header_string = 'xml'
        
        self.request.add_header("Accept", "application/" + header_string);

    def set_content_type_json_or_xml(self):
        header_string = 'json'

        if self.xml:
            header_string = 'xml'
        
        self.request.add_header("Content-type", "application/json")

    def is_administrator(self):
        return self.group == 'Administrator'

    @staticmethod
    def action_exists(action):
        '''
        Check if given action exist into API
        '''
        return action in Pyntervals.actions_allowed
   
    def filter_response(self, field, only_one = False):
        if self.python:
            if only_one:
                return json.loads(self.last_response)[field].pop()
            else:
                return json.loads(self.last_response)[field]
        else:
            return self.last_response


    def get_action(self, string_action, id = None):
        full_string_action = string_action;

        if id:
            full_string_action = string_action + '/' + id + '/'

        self.request = urllib2.Request(self.top_url + full_string_action)
        self.set_accept_json_or_xml()
        self.login()
        self.run()
        
        return self.filter_response(string_action, string_action in Pyntervals.actions_only_one)

    def action(self, string_action, method):
        self.request = urllib2.Request(self.top_url + string_action)
        self.set_accept_json_or_xml()
        
        if method.lower() in ['post', 'put']:
            self.set_content_type_json_or_xml()

        self.login()

    def put_action(self, string_action):
        '''
        TODO
        '''
        self.action(string_action, 'put')

    def post_action(self, string_action):
        '''
        TODO
        '''
        self.action(string_action, 'post')

    def delete_action(self, string_action, id):
        '''
        TODO
        '''

    def run(self):
        try:
            handle = urllib2.urlopen(self.request)
            self.last_response = handle.read()
        except IOError, e:
            self.errors.append("It looks like the token is wrong.")
            #sys.exit(1)

