import sys
import unittest
from importlib import import_module
from types import ModuleType
from unittest.mock import Mock, patch


cosmosis_stub = ModuleType("cosmosis")
cosmosis_stub.ClassModule = type("ClassModule", (), {})
with patch.dict(sys.modules, {"cosmosis": cosmosis_stub}):
    PowerModule = import_module("cosmosishood.power").PowerModule


class PowerModuleTests(unittest.TestCase):
    def test_init_reads_exponent_option(self):
        options = Mock()
        options.get_double.return_value = 2.5

        module = PowerModule(options)

        options.get_double.assert_called_once_with("exponent")
        self.assertEqual(module.exponent, 2.5)

    def test_execute_scales_and_raises_polynomial_value(self):
        module = PowerModule(Mock(get_double=Mock(return_value=2)))
        block = {
            ("power_module_coef", "power_module_param"): 3,
            ("poly", "y"): 4,
        }

        module.execute(block)

        self.assertEqual(block[("poly", "y")], 144)
