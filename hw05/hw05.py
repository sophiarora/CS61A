##############################################################
# An alternative implementation of the tree data abstraction #
##############################################################

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return {'<root>': root, '<branches>': branches}

def root(tree):
    return tree['<root>']

def branches(tree):
    return tree['<branches>']

def is_tree(tree):
    if type(tree) != dict or '<root>' not in tree or '<branches>' not in tree:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size)

def size(w):
    """Select the size of a weight."""
    assert is_weight(w)
    return root(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    if is_leaf(w):
        return True
    else:
        return False

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, u, v = examples()
    >>> print_tree(t)
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(t))
    3
      1
        2
      2
        1
    >>> print_tree(t)  # t should not change
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(v))
    9
      4
        3
          1
            2
          2
            1
      2
        6
          5
            1
          1
            5
              2
                3
              3
                2
    >>> print_tree(v)  # v should not change
    None
      4
        None
          1
            2
          2
            1
      2
        None
          5
            1
          1
            None
              2
                3
              3
                2
    """
    sides_new = []
    for s in sides(m):
        if is_weight(end(s)):
            sides_new += [s]
        else:
            sides_new += [side(length(s), with_totals(end(s)))]
    new_m = tree(total_weight(m),sides_new)
    return new_m


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    left_side = branches(m)[0]
    right_side = branches(m)[1]
    left_side_length = length(left_side)
    right_side_length = length(right_side)
    def side_weight(s):
        if is_weight(end(s)):
            return size(end(s))
        else:
            return total_weight(end(s))

    if left_side_length*side_weight(left_side) == right_side_length*side_weight(right_side):
        if is_weight(end(left_side)) and is_weight(end(right_side)):
            return True
        else:
            bal_list = [balanced(end(s)) for s in sides(m) if not is_weight(end(s))]
            if False not in bal_list:
                return True
            else:
                return False
    else:
        return False


############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    wrong_passwords = []
    def withdraw(amount, new_pass):
        nonlocal balance, wrong_passwords
        if len(wrong_passwords) < 3:
            if new_pass == password:
                if amount > balance:
                    return 'Insufficient funds'
                balance = balance - amount
                return balance
            else:
                wrong_passwords += [new_pass]
                return 'Incorrect password'
        else:
            print (str('"Your account is locked. Attempts: ') + str(wrong_passwords)+str('"'))
    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    new_w, correct_passwords = withdraw(0, old_password), []
    def new_withdraw(amount, password):
        nonlocal correct_passwords, first_password
        if password in correct_passwords:
            return withdraw(amount, first_password)
        else:
            return withdraw(amount, password)
    if type(new_w) == str:
        return new_w
    elif new_w != None:
        if len(correct_passwords) < 1:
            correct_passwords, first_password = [old_password], old_password
        correct_passwords += [new_password]
        return new_withdraw


###########
# Objects #
###########

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, vend_product, price):
        self.stock = 0
        self.product = vend_product
        self.price = price
        self.balance = 0
    def restock(self, amount):
        self.stock += amount
        return 'Current ' + str(self.product) + ' stock: ' + str(self.stock)
    def deposit(self, amount):
        if self.stock > 0:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)
        else:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'
    def vend(self):
        if self.stock == 0 and self.balance == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            price_gap = self.price - self.balance
            return 'You must deposit $' + str(price_gap) + ' more.'
        else:
            if self.balance == self.price:
                self.balance -= self.price
                self.stock -= 1
                return 'Here is your ' + str(self.product) + '.'
            else:
                balance_gap = self.balance - self.price
                self.balance = self.balance - (self.price + balance_gap)
                self.stock -= 1
                return 'Here is your ' + str(self.product) + ' and $' + str(balance_gap) + ' change.'

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, messager):
        self.messager = messager
        self.amount = 0
    def ask(self, *args):
        import re
        args_tuple = tuple(args)
        if len(args_tuple) > 1:
            second_arg = args_tuple[1]
        for arg in args:
            if type(arg) == int:
                self.amount = arg
        for arg in args:
            if 'please' in arg:
                please_mess = re.split('please ', arg)
                if please_mess[1] == '':
                    please_mess[1] = 'please ' + please_mess[2]
                if hasattr(self.messager, please_mess[1]):
                    if please_mess[1] == 'vend':
                        return getattr(self.messager, please_mess[1])()
                    elif please_mess[1] == 'ask':
                        return getattr(self.messager, 'ask')(second_arg, self.amount)
                    else:
                        return getattr(self.messager, please_mess[1])(self.amount)
                else:
                    return 'Thanks for asking, but I know not how to ' + please_mess[1] + '.'
            else:
                return 'You must learn to say please first.'





#############
# Challenge #
#############
