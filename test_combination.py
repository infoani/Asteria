import pytest
from main import *
from combination_algorithms import *

class TestCombinationAlgorithms:

    @pytest.mark.parametrize("input, output_arr", [
        (23, ('AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF')),
        (234, ('ADG', 'ADH', 'ADI', 'AEG', 'AEH', 'AEI', 'AFG', 'AFH', 'AFI', 'BDG', 'BDH', 'BDI', 'BEG', 'BEH', 'BEI', 'BFG', 'BFH', 'BFI', 'CDG', 'CDH', 'CDI', 'CEG', 'CEH', 'CEI', 'CFG', 'CFH', 'CFI'))
    ])
    def test_recursion_algo(self, input, output_arr):
        char_arr = char_from_number(input)
        
        com_o = CombineElements()
        output_test = com_o.combination(char_arr, CombineRecursion)

        assert output_test == output_arr

    @pytest.mark.parametrize("input, output_arr", [
        (23, ('AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF')),
        (234, ('ADG', 'ADH', 'ADI', 'AEG', 'AEH', 'AEI', 'AFG', 'AFH', 'AFI', 'BDG', 'BDH', 'BDI', 'BEG', 'BEH', 'BEI', 'BFG', 'BFH', 'BFI', 'CDG', 'CDH', 'CDI', 'CEG', 'CEH', 'CEI', 'CFG', 'CFH', 'CFI'))
    ])
    def test_iteration_algo(self, input, output_arr):
        char_arr = char_from_number(input)
        
        com_o = CombineElements()
        output_test = com_o.combination(char_arr, CombineIteration)

        assert output_test == output_arr