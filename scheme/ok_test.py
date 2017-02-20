>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> plus = PrimitiveProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, twos, env)
Choose the number of the correct choice:
0) 4
1) SchemeError

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> oddp = PrimitiveProcedure(scheme_oddp) # odd? procedure
>>> scheme_apply(oddp, twos, env)
Choose the number of the correct choice:
0) SchemeError
1) True
2) False

>>> from scheme import *
>>> env = create_global_frame()
>>> two = Pair(2, nil)
>>> eval = PrimitiveProcedure(scheme_eval, True) # eval procedure
>>> scheme_apply(eval, two, env) # be sure to check use_env

>>> from scheme import *
>>> env = create_global_frame()
>>> args = nil
>>> def make_scheme_counter():
...     x = 0
...     def scheme_counter():
...         nonlocal x
...         x += 1
...         return x
...     return scheme_counter
>>> counter = PrimitiveProcedure(make_scheme_counter()) # counter
>>> scheme_apply(counter, args, env) # only call procedure.fn once!

def retrieve_element(exp):
    values = []
    if len(exp) == 2:
        values = [exp.first]
        return values
    else:
        while scheme_listp(exp):
            exp = exp.first
        values += [exp]
        exp = exp.second
        values += [retrieve_element(exp)]
    return values
