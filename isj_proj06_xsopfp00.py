#!/usr/bin/env python3
import itertools
from collections import OrderedDict


def first_nonrepeating(string):
    """
    Find first character that occurs once in the given string
    :param string: string
    :return: character
    """
    if not isinstance(string, str):
        return None

    for char in string.strip():
        if string.count(char) == 1:
            return char
    return None


def combine4(numbers_list, result):
    """
    Finds equations, made by combinations of numbers, with given result
    :param numbers_list: list of 4 positive integers
    :param result: result of equations
    :return: list of equations
    """
    if not isinstance(numbers_list, list) or len(numbers_list) != 4:
        return list()
    if not isinstance(result, int):
        return list()

    for number in numbers_list:
        if not isinstance(number, int) or number < 1:
            return list()

    equations_list = []

    numbers_permutations = list(itertools.permutations(numbers_list))

    operators = ["+", "-", "*", "/"]
    operators_permutations = list(itertools.permutations(operators, 3))

    equations = ['%d %s %d %s %d %s %d',
                 '(%d %s %d) %s %d %s %d',
                 '%d %s (%d %s %d) %s %d',
                 '%d %s %d %s (%d %s %d)',
                 '(%d %s %d) %s (%d %s %d)',
                 '(%d %s %d %s %d) %s %d',
                 '%d %s (%d %s %d %s %d)',
                 '((%d %s %d) %s %d) %s %d',
                 '(%d %s (%d %s %d)) %s %d',
                 '%d %s ((%d %s %d) %s %d)',
                 '%d %s (%d %s (%d %s %d))']

    for num1, num2, num3, num4 in numbers_permutations:
        for oper1, oper2, oper3 in operators_permutations:
            for equation in equations:
                equation = equation % (num1, oper1, num2,
                                       oper2, num3, oper3, num4)
                try:
                    if eval(equation) == result:
                        equations_list.append(equation)
                except ZeroDivisionError:
                    pass

    return sorted(OrderedDict.fromkeys(equations_list))
