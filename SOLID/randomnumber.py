from random import randint

random_integer = randint(1, 3)

print(random_integer)

"""computers generate random numbers using two approaches:

Pseudo Random Number Generators (PRNGs):
    These generate random rumber by having a seed value (i.e, a number) which
is put into algorithm to generate a seemingly random number. These can be used in places
where it does not matter if random numbers get predicted. For example: random numbers 
generated for shuffling songs.

True Random Number Generators (TRNGs):
    They operate by measuring a well-controlled and specially prepared physical process. For example:
atmospheric conditions, radioactive decay which are random in nature. These numbers are put into an
algorithm to create true random numbers.


"""