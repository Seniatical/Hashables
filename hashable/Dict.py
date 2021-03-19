from .errors import (BadArgument,)

class Dict:
    
    def __init__(self, **_dict):
        if 'dict' in _dict:
            self.dict = _dict['dict']
        else:
            self.dict = _dict

    def __repr__(self):
        return '<Hashable Dict [{}]>'.format(self.dict)

    def __str__(self):
        return str(self.dict)

    def __format__(self, cls):
        return self.__repr__()

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value
        return self.dict

    def __delitem__(self, key):
        del self.dict[key]

    def __len__(self):
        return len(self.keys())

    def __contains__(self, key):
        return key in self.dict

    def __call__(self, key = None):
        if key:
            if key not in self.dict:
                return None
            return self.dict[key]
        return self.dict

    def items(self):
        return self.dict.items()

    def clear(self):
        self.dict = {}
        return self.dict

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def pop(self, key):
        value = self.dict[key]
        del self.dict[key]
        return value

    def fromkeys(self, iterable, values = None):
        if type(iterable) in [Dict, dict]:
            iterable = iterable.keys()
            values = values or iterable.values()
        else:
            iter(iterable)  ## Prevents stupid moves
        for i in range(len(iterable)):
            try:
                self.dict[iterable[i]] = values[i]
            except (KeyError, AttributeError):
                self.dict[iterable[i]] = None

    def sort(self):
        sorted_keys = sorted(self.dict, key=lambda key: str(key))
        temp = {}
        for key in sorted_keys:
            temp[key] = self.dict[key]
        self.dict = temp
        return self.dict

    def get_key(self, value):
        reversed = {v: k for k, v in self.dict.items()}
        return reversed[value]

    def get(self, key):
        if key not in self.dict:
            return None
        return self.dict[key]

    def value_sort(self):
        sorted_keys = sorted(self.dict.values())
        temp = {}
        for key in sorted_keys:
            temp[self.get_key(key)] = key
        self.dict = temp
        return self.dict

    def __add__(self, other):
        allowed = [Dict, dict, list, tuple, set]
        if type(other) not in allowed:
            raise TypeError('Object to add must derive from %s class not [%s]' % ([str(i).split()[-1][1:-2] for i in allowed], other.__class__.__name__))
        to_add = None
        if type(other) in [Dict, dict]:
            to_add = list(other.items())
        elif type(other) in [tuple, list, set]:
            for item in other:
                if type(item) in [tuple, list, set]:
                    if len(item) < 2:
                        raise BadArguement('item #%s key and pair value is too small' % (other.index(item) + 1))
                    elif len(item) > 2:
                        raise BadArguement('item #%s key and pair value is too large' % (other.index(item) + 1))
                else:
                    raise BadArguement('item #%s is not of satisfactory typing' % (other.index(item) + 1))
            to_add = other

        temp = list(self.dict.items())
        for item in to_add:
            temp.append(item)
        self.dict = dict(temp)
        return self.dict
