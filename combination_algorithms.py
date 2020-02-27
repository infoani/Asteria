from typing import List
from constant import *
from abc import ABCMeta, abstractmethod

class ICombination:

    @abstractmethod
    def combine(self, input_arr: List, permuted_list: List) -> List:
        pass

    @staticmethod
    def permute(element1, element2):
        if len(element1) == 0:
            return list(element2)
        if len(element2) == 0:
            return list(element1)
        return tuple([''.join([c1,c2]) for c1 in element1 for c2 in element2])


class CombineRecursion(ICombination):

    def combine(self, input_arr, permuted_list=[]):
        if len(input_arr) == 0:
            return permuted_list
    
        last_element_of_input_arr = input_arr.pop()
        permuted_list_new = self.permute(last_element_of_input_arr, permuted_list)
        return self.combine(input_arr, permuted_list_new)

class CombineIteration(ICombination):

    def combine(self, input_arr, permuted_list=[]):
        print("Iteration Algorithm Invoked", end="\n\n")
        while (input_arr):
            last_element_of_input_arr = input_arr.pop()
            permuted_list = self.permute(last_element_of_input_arr, permuted_list)

        return permuted_list

# helper class to implement algorithms
class CombineElements:

    def combination(self, input, combination_o):
        algo_base, = combination_o.__bases__
        if algo_base is not ICombination:
            raise TypeError(COMBINATION_ALGORITHM_EXPECTED_MSG)

        return combination_o().combine(input)