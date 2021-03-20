from ..errors import (BadArgument,)
from ..models.dict import (DictKeySet, DictValueSet, DictItemSet)

class Dict:
    
    def __init__(self, *args, **_dict):
        if 'dict' in _dict:
            self.dict = _dict['dict']
        else:
            self.dict = _dict

        if args:
            if type(args[0]) == dict:
                self.dict = args[0]
            else:
                self.dict = dict(args)

    def __repr__(self):
        return 'HashableDict([{}])'.format(self.dict)

    def __str__(self):
        return str(self.dict)

    def __format__(self, cls):
        return self.dict

    def __getitem__(self, key):
        indexes = list(self.keys())
        if type(key) == int:
            return self.dict[indexes[key]]
        
        if type(key) == slice:
            try:
                start = int(key.start)
            except (ValueError, TypeError):
                start = 0
            try:
                stop = int(key.stop)
            except (ValueError, TypeError):
                stop = len(indexes) ## basically the end
            try:
                step = int(key.stop)
            except (ValueError, TypeError):
                step = 1

            real = list(self.keys())[start:stop:step]
            return {key: self.dict[key] for key in real}

        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value
        return self.dict

    def __delitem__(self, key):
        del self.dict[key]

    def __len__(self):
        return len(list(self.keys()))

    def __contains__(self, key):
        if type(key) in [list, tuple]:
            sub_dict = dict([key])
            value = self.get(key[0])
            return value == sub_dict[key[0]]
        
        if type(key) == dict:
            new_value = list(key.values())[0]
            new_key = list(key.keys())[0]
            return self.get(new_key) == new_value

        if type(key) == Dict:
            new_key = list(key.keys())[0]
            new_value = list(key.values())[0]
            return self.get(new_key) == new_value
            
        return key in self.dict

    def __call__(self, key = None):
        if key:
            if key not in self.dict:
                return None
            return self.dict[key]
        return self.dict

    def __eq__(self, other):
        if type(other) == dict:
            return self.dict == other
        elif type(other) == Dict:
            return self.dict == other.dict
        raise TypeError('cannot compare %s with type dict' % other.__class__.__name__)

    def __nq__(self, other):
        if type(other) == dict:
            return self.dict != other
        elif type(other) == Dict:
            return self.dict != other.dict
        raise TypeError('cannot compare %s with type dict' % other.__class__.__name__)

    def __gt__(self, other):
        if type(other) == dict:
            return self.__len__() > len(list(other.keys()))
        elif type(other) == Dict:
            return self.__len__() > len(other)
        raise TypeError('cannot compare %s with type dict' % other.__class__.__name__)

    def __lt__(self, other):
        if type(other) == dict:
            return self.__len__() < len(list(other.keys()))
        elif type(other) == Dict:
            return self.__len__() < len(other)
        raise TypeError('cannot compare %s with type dict' % other.__class__.__name__)

    def __add__(self, other):
        allowed = [Dict, dict, list, tuple]
        if type(other) not in allowed:
            raise TypeError('Object to add must derive from %s class not [%s]' % ([str(i).split()[-1][1:-2] for i in allowed], other.__class__.__name__))
        to_add = None
        if type(other) in [Dict, dict]:
            to_add = list(other.items())
        elif type(other) in [tuple, list]:
            for item in other:
                if type(item) in [tuple, list]:
                    if len(item) < 2:
                        raise BadArgument('item #%s key and pair value is too small' % (other.index(item) + 1))
                    elif len(item) > 2:
                        raise BadArgument('item #%s key and pair value is too large' % (other.index(item) + 1))
                else:
                    raise BadArgument('item #%s is not of satisfactory typing' % (other.index(item) + 1))
            to_add = other

        temp = list(self.dict.items())
        for item in to_add:
            temp.append(item)
        self.dict = dict(temp)
        return self.dict

    def items(self):
        return self.dict.items()

    def clear(self):
        self.dict = {}
        return self.dict

    def keys(self):
        return DictKeySet(list(self.dict.keys()))

    def values(self):
        return DictValueSet(list(self.dict.values()))

    def items(self):
        return DictItemSet(list(self.dict.items()))

    def pop(self, key, is_index = False, is_key = True):
        if is_index:
            value = self.__getitem__(int(key))
            key = self.get_key(value)

        if not is_key:
            key = self.get_key(key)
            value = key
            
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
            except KeyError:
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

    def get_nested(self, key):
        items = self.items()
        dicts = []
        for _key, value in items:
            if type(value) in [Dict, dict]:
                dicts.append(value)

        for sub_dict in dicts:
            if key in sub_dict:
                return sub_dict
        return False

    def value_sort(self):
        sorted_keys = sorted(self.dict.values())
        temp = {}
        for key in sorted_keys:
            temp[self.get_key(key)] = key
        self.dict = temp
        return self.dict

    def index(self, value, start: int = 0, end: int = None, key=False, as_dict=True):
        if not key:
            if not end:
                values = list(self.values())[start:]
            else:
                values = list(self.values())[start:end]
        else:
            if not end:
                values = list(self.keys())[start:]
            else:
                values = list(self.keys())[start:end]
        for _value in values:
            if _value == value:
                if not key:
                    new_key = self.get_key(_value)
                else:
                    new_key = self.get(_value)
                
                if as_dict:
                    return {
                        'index': values.index(_value, 0),
                        'value': new_key,
                        }
                else:
                    return new_key
        raise IndexError('Cannot find %s in the dict sequence' % value)
