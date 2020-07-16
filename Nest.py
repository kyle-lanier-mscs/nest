# Author: Kyle Lanier 12/11/2017

import json
import datetime

# Nest flattens nested objects into one k v set
class Nest(object):

    def to_json(self, object):
        try:
            return json.loads(object)
        except TypeError:
            pass
        except ValueError:
            pass
        return json.loads(json.dumps(object, cls=Nest.Encoder, indent=4))

    # Create an encoder subclassing JSON.encoder.
    # Make this encoder aware of our classes (e.g. datetime.datetime objects) 
    class Encoder(json.JSONEncoder):
        def default(self, object):
            if isinstance(object, datetime.datetime):
                return object.isoformat()
            else:
                return json.JSONEncoder.default(self, object)

    # metaclass object used to provide attributes to the parent object
    class Meta(object):
        def __init__(self, object, to_json, symbol='_'):

            # function is recursively called to concatenate nested keys
            def inspect(object, priorKey=None):

                # copy the prior key-list, else make a new list
                priorKey = priorKey[:] if priorKey else []

                object = to_json(object)

                # if our new value is a dictionary
                if isinstance(object, dict):

                    for newKey, value in list(object.items()):

                        value = to_json(value)

                        # if the next value is a dictionary
                        if isinstance(value, dict):

                            # concatenate the keys
                            for next_object in inspect(value, priorKey + [newKey]):
                                # yield returns an iterator
                                yield next_object

                        # if the next value is a list
                        elif isinstance(value, list) or isinstance(value, tuple):

                            # recurse through and concatenate the list indexes to the prior keys
                            for next_object in inspect({str(v): k for v, k in enumerate(value)}, priorKey + [newKey]):
                                # yield returns an iterator
                                yield next_object

                        # next value is not a key or a lst, return the current value
                        else:

                            # yield returns an iterator
                            yield priorKey + [newKey, value]

                # if our value is an immutable python object
                elif isinstance(object, list) or isinstance(object, tuple):

                    # recuse through and concatenate the tuple keys to the prior keys
                    for next_object in inspect({str(k): v for v, k in enumerate(object)}, priorKey):

                        # yield returns an iterator
                        yield next_object

                # neither dictionary,  list, or tuple, return the value
                else:
                    # yield returns an iterator
                    yield priorKey + [object]


            # while recursing through all objected keys
            for next_object in inspect(object):
                for L in [next_object]:
                    # append a '_' inbetween each concatenated key
                    # set the new key value attributes of the meta class
                    self.__setattr__(symbol.join(L[:-1]), L[-1])

    def __init__(self, object, symbol='_'):
        object = self.to_json(object)
        
        # move the attributes from the metaclass into the parent class
        for set in vars(self.Meta(object, self.to_json, symbol)).items():
            self.__setattr__(set[0], set[1])
    
    # for Nest.getAttribute
    def __getattr__(self, item):
        d = {}
        for k, v in list(vars(self).items()):
            if item in k:
                d[k] = v

        if len(d) == 1:
            return list(d.values())[0]
        return d

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
