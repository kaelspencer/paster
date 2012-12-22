import json
import os
import sublime
import sublime_plugin
import urllib2

class PasterCommand(sublime_plugin.TextCommand):
    text = None
    title = None
    syntax = None
    url = 'http://localhost:8000/p/api/paste/'

    def run(self, edit):
        self.get_selected_text()
        self.get_title()
        self.get_syntax()

        self.paste()

    def paste(self):
        data = json.dumps({
            'title': self.title,
            'text': 'test data',
            'syntax': self.syntax
            })
        print data

        try:
            request = urllib2.Request(self.url, data)
            response = urllib2.urlopen(request)

            print response.getcode()
            print response.read()
        except Exception, e:
            print e

    def get_selected_text(self):
        selected_region = self.view.sel()[0]

        if 0 == selected_region.size():
            self.text = self.view.substr(sublime.Region(0, self.view.size()))
        else:
            self.text = self.view.substr(selected_region)

    def get_title(self):
        self.title = self.view.file_name()

        if self.title is not None:
            self.title = os.path.split(self.title)[1]
        else:
            self.title = 'Paste from Sublime Text'

    def get_syntax(self):
        self.syntax = self.view.settings().get('syntax')
        self.syntax = os.path.split(self.syntax)[1]
        self.syntax = os.path.splitext(self.syntax)[0]
