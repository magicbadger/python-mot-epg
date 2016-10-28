import unittest

from msc import bitarray_to_hex
from mot import HeaderParameter
from mot.epg import ScopeId

class ScopeIdTest(unittest.TestCase):

    def test_si_scope(self):
        id = ScopeId(0xe1, 0xc185)
        assert bitarray_to_hex(id.encode()) == 'E7 03 E1 C1 85'
        HeaderParameter.from_bits(id.encode())
        
    def test_pi_scope(self):
        id = ScopeId(0xe1, 0xc185, 0xc586, 0)
        assert bitarray_to_hex(id.encode()) == 'E7 06 40 E1 C1 85 C5 86'
        HeaderParameter.from_bits(id.encode())

if __name__ == "__main__":
    unittest.main()
