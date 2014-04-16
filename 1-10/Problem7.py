from CommonUtilities import primes
from itertools import islice


print list(islice(primes(), 10001))[-1]