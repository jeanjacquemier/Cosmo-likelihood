import sys
import unittest
from importlib import import_module
from types import ModuleType
from unittest.mock import Mock, patch


cosmosis_stub = ModuleType("cosmosis")
cosmosis_stub.ClassModule = type("ClassModule", (), {})
with patch.dict(sys.modules, {"cosmosis": cosmosis_stub}):
    PolyModule = import_module("cosmosishood.polynome").PolyModule


class PolynomeModuleTests(unittest.TestCase):
    def test_init_reads_exponent_option(self):
        options = Mock()
        options.get_int.return_value = 3

        module = PolyModule(options)
        options.get_int.assert_called_once_with("degree")
        
        self.assertEqual(module.degree, 3)

    
    def test_execute(self):
        module = PolyModule(Mock(get_int=Mock(return_value=2)))

        block = {
            ("coefficients", "param_0"): 1,
            ("coefficients", "param_1"): 2,
            ("coefficients", "param_2"): 3,
            ("poly", "y"): 4,
        }

        module.execute(block)
    

# coef  = block['power_module_coef', 'power_module_param']
# coef  = block['coefficients', f'param_{i}']