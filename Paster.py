import os
import sublime
import sublime_plugin

class PasterCommand(sublime_plugin.TextCommand):
    text = None
    title = None
    syntax = None

    def run(self, edit):
        self.get_selected_text()
        self.get_title()
        self.get_syntax()

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
