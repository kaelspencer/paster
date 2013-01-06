paster
======

A plugin for Sublime Text 2 that pastes to [my site]. The plugin determines which syntax Sublime Text is using and then attempts to match it to something the paste site supports (with [Pygments]). Anything unknown defaults to plain text.

There aren't any settings. After selecting some text, the context menu contains "Paste to Web" which triggers the paste. If no text is selected the entire document is used. The title of the paste is that of the document. A URL to view the paste is placed into the clipboard.

Installation
------------

To install, simply copy the *paster* folder to Sublime's [package directory]. I'll work on getting it into Package Control at some point.

 [my site]: http://kaelspencer.com
 [Pygments]: http://pygments.org
 [package directory]: http://docs.sublimetext.info/en/latest/basic_concepts.html#the-packages-directory
