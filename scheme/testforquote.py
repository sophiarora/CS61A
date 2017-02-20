def retrieve_element(exp):
    values = []
    if len(exp) == 2:
        values += [exp.first]
        return values
    else:
        while scheme_listp(exp.first):
            exp = exp.first
        values += [exp.first]
        if exp.second != nil:
            exp = exp.second
            values += retrieve_element(exp)
            return values
        return values

def retrieve_element(exp):
    values = []
    if len(exp) == 2:
        values += [exp.first]
        return values
    else:
        while scheme_listp(exp.first):
            exp = exp.first
        values += [exp.first]
        if exp.second != nil:
            exp = exp.second
            values += retrieve_element(exp)
            return values
        return values
elements = retrieve_element(expressions)
if 'quote' in elements:
    quoted = expressions
    if quoted.first == 'quote':
        quoted = expressions.second
    else:
        quoted = expressions.first
    result = do_quote_form(quoted, env)
    return result
else:
