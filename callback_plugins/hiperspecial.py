from ansible.plugins.callback import CallbackBase
from art import *

class CallbackModule(CallbackBase):
    def v2_playbook_on_stats(self, stats):
        print(text2art("HIPER", font="block"))