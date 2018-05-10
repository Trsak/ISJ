#!/usr/bin/env python3


def can_be_a_set_member_or_frozenset(item):
    """
    Checks if item can be set member and if it can't, returns frozenset of it
    :param item: item to be checked
    :return: if item can be member of a set, then item is returned, otherwise returns frozenset of item
    """
    try:
        # Just try to add item to the set
        set_try = set()
        set_try.add(item)
        return item
    except TypeError:
        # Item could not be added to set, return frozenset of it
        return frozenset(item)


def all_subsets(lst):
    """
    Takes list of items and returns list with set of all subsets
    :param lst: list of items
    :return: list with set of all subsets of items
    """
    subsets = [[]]
    # Loop through all items in list and add item to all subsets in subsets list
    for item in lst:
        subsets += [subset + [item] for subset in subsets]
    return subsets


def all_subsets_excl_empty(*items, exclude_empty=True):
    """
    Calls all_subsets functions and returns list with set of all subsets.
    If exclude_empty parameter is set to True, then removes empty list from it.
    :param items: list of items
    :param exclude_empty: determine whether exclude empty list or not
    :return: list with set of all subsets of items, if exclude_empty is True, then empty list is not included
    """
    subsets = all_subsets(items)
    if exclude_empty:
        subsets.remove([])

    return subsets


def test():
    """
    Test all functions using assert
    """
    # Tests for can_be_a_set_member_or_frozenset
    assert can_be_a_set_member_or_frozenset(1) == 1
    assert can_be_a_set_member_or_frozenset((1, 2)) == (1, 2)
    assert can_be_a_set_member_or_frozenset([1, 2]) == frozenset([1, 2])
    # Tests for all_subsets
    assert all_subsets(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'],
                                            ['a', 'b', 'c']]
    # Tests for all_subsets_excl_empty
    assert all_subsets_excl_empty('a', 'b', 'c') == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'],
                                                     ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty=True) == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'],
                                                                         ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty=False) == [[], ['a'], ['b'], ['a', 'b'], ['c'],
                                                                          ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]


if __name__ == '__main__':
    test()
