# Author: Kyle Lanier 12/11/2017

import json
import datetime

# Nest flattens nested objects into one k v set
class Nest(object):

    def is_json(myjson):
        try:
            json.loads(myjson)
        except TypeError:
            return False
        except ValueError:
            return False
        return True

    # Create an encoder subclassing JSON.encoder.
    # Make this encoder aware of our classes (e.g. datetime.datetime objects) 
    class Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.isoformat()
            else:
                return json.JSONEncoder.default(self, obj)

    # metaclass object used to provide attributes to the parent object
    class Meta(object):
        def __init__(self, nest, symbol='_'):

            # function is recursively called to concatenate nested keys
            def recursion(nest, priorKey=None):

                # copy the prior key-list, else make a new list
                priorKey = priorKey[:] if priorKey else []

                if Nest.is_json(nest):
                    nest = json.loads(nest)

                # if our new value is a dictionary
                if isinstance(nest, dict):

                    for newKey, value in list(nest.items()):

                        # value = [value, json.loads(value)][int(is_json(value))]
                        if Nest.is_json(value):
                            value = json.loads(value)

                        # if the next value is a dictionary
                        if isinstance(value, dict):

                            # concatenate the keys
                            for recursed in recursion(value, priorKey + [newKey]):
                                # yield returns an iterator
                                yield recursed

                        # if the next value is a list
                        elif isinstance(value, list) or isinstance(value, tuple):

                            # recurse through and concatenate the list indexes to the prior keys
                            for recursed in recursion({str(v): k for v, k in enumerate(value)}, priorKey + [newKey]):
                                # yield returns an iterator
                                yield recursed

                        # next value is not a key or a lst, return the current value
                        else:

                            # yield returns an iterator
                            yield priorKey + [newKey, value]

                # if our value is an immutable python object
                elif isinstance(nest, list) or isinstance(nest, tuple):

                    # recuse through and concatenate the tuple keys to the prior keys
                    for recursed in recursion({str(k): v for v, k in enumerate(nest)}, priorKey):

                        # yield returns an iterator
                        yield recursed

                # neither dictionary,  list, or tuple, return the value
                else:
                    # yield returns an iterator
                    yield priorKey + [nest]

            # while recursing through all nested keys
            # append a '_' inbetween each concatenated key
            # set the new key value attributes of the meta class
            list([self.__setattr__(symbol.join(L[:-1]), L[-1]) for L in [x for x in recursion(nest)]])

    def __init__(self, nest, symbol='_'):
        if Nest.is_json(nest):
            nest = json.loads(nest)
        else:
            nest = json.loads(json.dumps(nest, cls=Nest.Encoder, indent=4))
        # move the attributes from the metaclass into the parent class
        list([self.__setattr__(k_v[0], k_v[1]) for k_v in iter(list(vars(self.Meta(nest, symbol)).items()))])

    # for Nest.getAttribute
    def __getattr__(self, item):
        d = {}
        for k, v in list(vars(self).items()):
            if item in k:
                d[k] = v

        attr = vars(self.Meta(d))

        try:
            # if the item was found
            return [attr, list(attr.values())[0]][int(len(attr) == 1)]
        except:
            # provided key or subkey item was not found
            return None

    # for Nest['myItem']
    def __getitem__(self, item):
        return getattr(self, item)

    # standard dictionary.values()
    def values(self):
        return list(vars(self).values())
    
    # standard dictionary.keys()
    def keys(self):
        return list(vars(self).keys())

    # standard pyhton3.items()
    def items(self):
        return vars(self)
