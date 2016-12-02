import sublime_plugin
import re
from sublime import Region

re_quotes = re.compile("^(['\"`])(.*)\\1$")
quoteList = ['\'', '"', '`']


class ToggleQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        v = self.view
        if v.sel()[0].size() == 0:
            v.run_command('expand_selection', {'to': 'scope'})

        for sel in v.sel():
            text = v.substr(sel)
            res = re_quotes.match(text)
            if not res:
                #  the current selection doesn't begin and end with a quote.
                #  let's expand the selection one character each direction and try again
                sel = Region(sel.begin() - 1, sel.end() + 1)
                text = v.substr(sel)
                res = re_quotes.match(text)
                if not res:
                    #  still no match... skip it!
                    continue
            oldQuotes = res.group(1)
            if 'key' in kwargs:
                newQuotes = kwargs['key']
            else:
                newQuotes = quoteList[(quoteList.index(oldQuotes) + 1) % len(quoteList)]
            text = res.group(2)
            text = text.replace(newQuotes, "\\" + newQuotes)
            text = text.replace("\\" + oldQuotes, oldQuotes)
            text = newQuotes + text + newQuotes
            v.replace(edit, sel, text)


# 'te\'st'
# 'te"st'
# 'test'
# 'te\'st'
# 'te"st'
# "te\"st"
# "te'st"
# `te"s't`
