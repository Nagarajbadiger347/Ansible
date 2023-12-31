from ansible.plugins.callback import CallbackBase

import json
class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stout'
    CALLBACK_NAME = 'json_stat'
    CALLBACK_NEEDS_ENABLED = True

    def v2_playbook_on_stats(self, stats):
        output = {}
        for h in stats.processed.keys():
            t = stats.summarize(h)
            output[h] = {
                'sucessful': t['ok'],
                'failed': t['failures'],
                'skipped': t['skipped'],
            }

        self._display.display(json.dumps(output, indent=2))
       