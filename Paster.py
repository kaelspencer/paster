import json
import os
import sublime
import sublime_plugin
import urllib2

class PasterCommand(sublime_plugin.TextCommand):
    text = None
    title = None
    lexer = None
    domain = 'http://kaelspencer.com'
    url = domain + '/p/api/paste/'

    def run(self, edit):
        self.get_selected_text()
        self.get_title()
        self.get_lexer()

        self.paste()

    def paste(self):
        data = json.dumps({
            'title': self.title,
            'text': self.text,
            'lexer': self.lexer
            })

        try:
            request = urllib2.Request(self.url, data)
            response = urllib2.urlopen(request)

            paste_url = self.domain + response.read()

            print 'Paste response: ' + str(response.getcode())
            print 'Paste URL: ' + paste_url
            sublime.set_clipboard(paste_url)
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

    def get_lexer(self):
        syntax = self.view.settings().get('syntax')
        syntax = os.path.split(syntax)[1]
        syntax = os.path.splitext(syntax)[0]

        # Check if the syntax is in the dictionary. Default to 'text' if it isn't.
        if syntax in syntax_to_lexers:
            self.lexer = syntax_to_lexers[syntax]
        else:
            self.lexer = 'text'

        print syntax + ' -> ' + self.lexer


# This dictionary contains known Sublime Text syntaxs mapped to corresponding lexers
# used by the paste destination. A few point to 'text' as there is no equivalent.
syntax_to_lexers = {
    'ActionScript': 'as',
    'AppleScript': 'applescript',
    'ASP': 'aspx-cs',
    'HTML-ASP': 'aspx-cs',
    'Batch File': 'bat',
    'Build': 'text',
    'C#': 'csharp',
    'C++': 'cpp',
    'C': 'c',
    'Clojure': 'clojure',
    'CSS': 'css',
    'D': 'd',
    'Diff': 'diff',
    'Erlang': 'erlang',
    'HTML (Erlang)': 'erlang',
    'Go': 'go',
    'DOT': 'text',
    'Groovy': 'text',
    'Haskell': 'haskell',
    'Literate Haskell': 'lhs',
    'HTML': 'html',
    'Java Server Pages (JSP)': 'jsp',
    'Java': 'java',
    'JavaDoc': 'text',
    'JavaProperties': 'text',
    'JavaScript': 'js',
    'JSON': 'text',
    'jQueryJavaScript': 'js',
    'Bibtex': 'tex',
    'LaTeX Beamer': 'tex',
    'LaTeX Log': 'tex',
    'LaTeX Memoir': 'tex',
    'LaTeX': 'tex',
    'TeX Math': 'tex',
    'TeX': 'tex',
    'Lisp': 'common-lisp',
    'Lua': 'lua',
    'Makefile': 'make',
    'Markdown': 'text',
    'MultiMarkdown': 'text',
    'Matlab': 'matlab',
    'Objective-C++': 'objective-c',
    'Objective-C': 'objective-c',
    'camlp4': 'text',
    'OCaml': 'ocaml',
    'OCamllex': 'ocaml',
    'OCamlyacc': 'ocaml',
    'Perl': 'perl',
    'PHP': 'php',
    'Python': 'python',
    'Regular Expressions (Python)': 'python',
    'R Console': 'text',
    'R': 'text',
    'Rd (R Documentation)': 'text',
    'HTML (Rails)': 'html',
    'JavaScript (Rails)': 'js-erb',
    'Ruby Haml': 'rb',
    'Ruby on Rails': 'rb',
    'SQL (Rails)': 'sql',
    'RegExp': 'text',
    'reStructuredText': 'rst',
    'Ruby': 'rb',
    'Scala': 'scala',
    'Shell-Unix-Generic': 'console',
    'SQL': 'sql',
    'HTML (Tcl)': 'tcl',
    'Tcl': 'tcl',
    'Plain text': 'text',
    'Textile': 'text',
    'XML': 'xml',
    'XSL': 'xslt',
    'YAML': 'yaml',
}
