from ansible import errors
from _collections_abc import MutableMapping

def is_large(item):
    '''Determine instance_type is large , 2xlarge, etc'''
    if not isinstance(item, MutableMapping):
        raise errors.AnsibleFilterError("the 'is_large' test expects a string or dictionary")
    if not 'value' in item:
        raise errors.AnsibleFilterError("unexpected dictionary")
    value = item.get('value', ())
    if not 'instance_type' in value:
        raise errors.AnsibleFilterError("no 'instance_type was found")
    return 'large' in value.get('instance_type', '')

class TestModule(object):
    '''custom ansible task'''
    def tests(self):
        return {
            'is_large': is_large,
            
        }

