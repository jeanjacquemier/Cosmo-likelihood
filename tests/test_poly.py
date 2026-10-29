import sys
import unittest
from importlib import import_module
from types import ModuleType
from unittest.mock import Mock, patch

import numpy as np


cosmosis_stub = ModuleType("cosmosis")
cosmosis_stub.datablock = type("datablock", (), {})
with patch.dict(sys.modules, {"cosmosis": cosmosis_stub}):
    polynome = import_module("cosmosishood.polynome")


class PolynomeTests(unittest.TestCase):
    def test_setup_reads_degree_and_returns_config(self):
        config = Mock()
        config.get_int.return_value = 2

        result = polynome.setup(config)

        config.get_int.assert_called_once_with("degree")
        self.assertEqual(result, {"degree": 2})

    def test_execute_builds_polynomial_points_and_returns_success(self):
        degree = 2
        sample = {
            ("coefficients", "param_0"): 1.0,
            ("coefficients", "param_1"): 2.0,
            ("coefficients", "param_2"): 3.0,
        }

        with patch("builtins.print"):
            result = polynome.execute(sample, {"degree": degree})

        expected_x = np.linspace(0, 1, 1000)
        expected_y = 1.0 + 2.0 * expected_x + 3.0 * expected_x**2
        self.assertEqual(result, 0)
        np.testing.assert_array_equal(sample[("poly", "x")], expected_x)
        np.testing.assert_allclose(sample[("poly", "y")], expected_y)