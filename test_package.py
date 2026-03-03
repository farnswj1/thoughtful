import unittest

from package import sort, STANDARD, SPECIAL, REJECTED


class TestPackageTypes(unittest.TestCase):
    """Test cases for the package results."""

    def test_standard_constant(self) -> None:
        self.assertEqual(STANDARD, "standard")

    def test_special_constant(self) -> None:
        self.assertEqual(SPECIAL, "special")

    def test_rejected_constant(self) -> None:
        self.assertEqual(REJECTED, "rejected")


class TestPackageSort(unittest.TestCase):
    """Test cases for the package sorting function."""

    def test_standard_package(self) -> None:
        result = sort(50.0, 50.0, 50.0, 10.0)
        self.assertEqual(result, STANDARD)

    def test_large_standard_package(self) -> None:
        result = sort(99.999999999, 100.0, 100.0, 19.999999999)
        self.assertEqual(result, STANDARD)

    def test_special_bulky_package_volume(self) -> None:
        result = sort(100.0, 100.0, 100.0, 10.0)
        self.assertEqual(result, SPECIAL)

    def test_special_bulky_package_width(self) -> None:
        result = sort(150.0, 50.0, 50.0, 10.0)
        self.assertEqual(result, SPECIAL)

    def test_special_bulky_package_height(self) -> None:
        result = sort(50.0, 150.0, 50.0, 10.0)
        self.assertEqual(result, SPECIAL)

    def test_special_bulky_package_length(self) -> None:
        result = sort(50.0, 50.0, 150.0, 10.0)
        self.assertEqual(result, SPECIAL)

    def test_special_heavy_package(self) -> None:
        result = sort(50.0, 50.0, 50.0, 20.0)
        self.assertEqual(result, SPECIAL)

    def test_rejected_package(self) -> None:
        result = sort(100.0, 100.0, 100.0, 20.0)
        self.assertEqual(result, REJECTED)

    def test_invalid_width(self) -> None:
        with self.assertRaises(ValueError):
            sort(0.0, 50.0, 50.0, 10.0)

    def test_invalid_height(self) -> None:
        with self.assertRaises(ValueError):
            sort(50.0, 0.0, 50.0, 10.0)

    def test_invalid_length(self) -> None:
        with self.assertRaises(ValueError):
            sort(50.0, 50.0, 0.0, 10.0)

    def test_invalid_mass(self) -> None:
        with self.assertRaises(ValueError):
            sort(50.0, 50.0, 50.0, 0.0)

    def test_minimum_valid_package(self) -> None:
        result = sort(0.000000001, 0.000000001, 0.000000001, 0.000000001)
        self.assertEqual(result, STANDARD)
