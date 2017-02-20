## Trees ##

# Q4
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    return tree(username, [tree('pop',
                              [tree('justin bieber',
                                  [tree('single',
                                      [tree('what do you mean?')])]),
                               tree('2015 pop mashup')]),
                          tree('trance',
                              [tree('darude',
                                  [tree('sandstorm')])])])



# Q5
def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    count_song = 0
    if is_leaf(t):
        count_song += 1
    else:
        count_song = sum([num_songs(branch) for branch in branches(t)])
    return count_song


# Q6
def find(t, target):
    """Returns True if t contains a node with the value TARGET and False
    otherwise.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> find(my_account, 'korean')
    True
    >>> find(my_account, 'blank space')
    True
    >>> find(my_account, 'bad blood')
    False
    """
    def count_true(tree, value):
        c_true = 0
        if root(tree) == value:
            c_true += 1
        else:
            c_true = sum([count_true(branch, value) for branch in branches(tree)])
        return c_true
    if count_true(t, target) == 1:
        return True
    else:
        return False

# Q7
def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    new_branches = []
    if find(t, category):
        if root(t) == category:
            new_tree = tree(root(t), branches(t) + [tree(song)])
        else:
            for branch in branches(t):
                if find(branch, category):
                    new_branches += [add_song(branch, song, category)]
                else:
                    new_branches += [branch]
            new_tree = tree(root(t), new_branches)
    else:
        print('No such category')
    return new_tree


# Q8
def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    new_branches = []
    if find(t, target):
        if root(t) == target:
            new_tree = []
        else:
            for branch in branches(t):
                if find(branch, target) and root(branch) != target:
                    new_branches += [delete(branch, target)]
                elif find(branch, target) and root(branch) == target:
                    new_branches += delete(branch, target)
                else:
                    new_branches += [branch]
            new_tree = tree(root(t), new_branches)
    else:
        print('No such category')
    return new_tree

# ADT
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)


def root(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
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
