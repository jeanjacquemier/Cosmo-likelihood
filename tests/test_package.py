import unittest


class PackageTests(unittest.TestCase):
    def test_package_has_version(self):
        import cosmosishood

        self.assertEqual(cosmosishood.__version__, "0.1.0")
