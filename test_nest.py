from Nest import Nest
from Examples.run_instances import RunInstances
from pprint import pprint


# Lets de-nest our RunInstances event
myNest = Nest(RunInstances)

# print everything
# pprint(myNest.items())

# Get just the values for any concatenated key
# that contains 'Arn'

pprint(myNest['Arn'])