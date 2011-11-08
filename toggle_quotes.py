import sublime_plugin
import re
import string


class ToggleQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        for sel in v.sel():
            text = v.substr(sel)
            res = re.match("^(['\"])(.*)\\1$", text)
            if not res:
                continue
            oldQuotes = res.group(1)
            newQuotes = "'" if oldQuotes == '"' else '"'
            text = res.group(2)
            text = string.replace(text, newQuotes, "\\" + newQuotes)
            text = string.replace(text, "\\" + oldQuotes, oldQuotes)
            text = newQuotes + text + newQuotes
            v.replace(edit, sel, text)


# "te'st"
# "te\"st"
# 'test'
# "te'st"
# "te\"st"
# 'te"st'
# 'te\'st'
