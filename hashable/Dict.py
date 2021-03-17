from .errors import (BadArgument,)

class Dict:
    def __init__(self, **dict):
        if 'dict' in dict:
            self.dict = dict['dict']
        else:
            self.dict = dict

    def __repr__(self):
        return '<Hashable Dict [{}]>'.format(self.dict)

    def __str__(self):
        return str(self.dict)

    def __format__(self, cls):
        return self.__repr__()

    def items(self):
    	return self.dict.items()

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

new = Dict(dict={1: 2, 3: 4})
new + Dict(y=10, x=5)
print(new)
