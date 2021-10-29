import unittest

# import pytest
from spark_contract_testing import loadContracts

class TestContract(unittest.TestCase):
    def testLoadContracts(self):
        schema = loadContracts("test")
        self.assertEqual(schema, "foo")
        return "foo"
