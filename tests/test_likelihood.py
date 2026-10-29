import sys
import unittest
from importlib import import_module
from types import ModuleType
from unittest.mock import patch

import numpy as np


class GaussianLikelihoodStub:
    def __init__(self, options):
        self.options = options


cosmosis_stub = ModuleType("cosmosis")
cosmosis_stub.GaussianLikelihood = GaussianLikelihoodStub
with patch.dict(sys.modules, {"cosmosis": cosmosis_stub}):
    Likelihood = import_module("cosmosishood.likelihood").Likelihood


class LikelihoodTests(unittest.TestCase):
    def test_init_passes_options_to_parent(self):
        options = {"noise_level": 2.0}

        likelihood = Likelihood(options)

        self.assertIs(likelihood.options, options)

    def test_build_data_returns_expected_points(self):
        likelihood = Likelihood({"noise_level": 1.0})

        x, y = likelihood.build_data()

        expected_x = np.array([0.2, 0.31, 0.44, 0.77, 0.9])
        expected_y = (1.4 * expected_x**2 - 3.1 * expected_x - 0.8) ** 2
        np.testing.assert_array_equal(x, expected_x)
        np.testing.assert_allclose(y, expected_y)

    def test_build_covariance_scales_noise_and_returns_diagonal(self):
        likelihood = Likelihood({"noise_level": 2.0})

        covariance = likelihood.build_covariance()
        sigma = np.array([0.05, 0.06, 0.04, 0.03, 0.1]) * 2.0

        np.testing.assert_allclose(covariance, np.diag(sigma**2))
        np.testing.assert_array_equal(covariance - np.diag(np.diag(covariance)), 0)
