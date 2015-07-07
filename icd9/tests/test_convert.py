import icd9
from unittest import TestCase, TestLoader, TestSuite


class DecimalToShortTestCase(TestCase):

    def test_one_major_no_minor(self):
        self.assertEqual(icd9.decimal_to_short('1'), '001')

    def test_one_major_one_zero_minor(self):
        self.assertEqual(icd9.decimal_to_short('1.0'), '0010')

    def test_one_major_one_minor(self):
        self.assertEqual(icd9.decimal_to_short('1.1'), '0011')

    def test_one_major_two_minors(self):
        self.assertEqual(icd9.decimal_to_short('1.23'), '00123')

    def test_two_major_no_minor(self):
        self.assertEqual(icd9.decimal_to_short('22'), '022')
        self.assertEqual(icd9.decimal_to_short('81'), '081')

    def test_two_major_one_minor(self):
        self.assertEqual(icd9.decimal_to_short('81.1'), '0811')

    def test_two_major_two_minor(self):
        self.assertEqual(icd9.decimal_to_short('81.23'), '08123')

    def test_three_major_no_minor(self):
        self.assertEqual(icd9.decimal_to_short('345'), '345')
        self.assertEqual(icd9.decimal_to_short('991'), '991')

    def test_three_major_one_minor(self):
        self.assertEqual(icd9.decimal_to_short('991.1'), '9911')

    def test_three_major_two_minor(self):
        self.assertEqual(icd9.decimal_to_short('991.23'), '99123')


class DecimalToPartsTestCase(TestCase):

    def test_one_zero(self):
        self.assertTupleEqual(icd9.decimal_to_parts('0'), ('000', ''))

    def test_many_zeros(self):
        self.assertTupleEqual(icd9.decimal_to_parts('000'), ('000', ''))

    def test_vcode_major_one_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('V1.2'), ('V01', '2'))

    def test_one_major_one_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('1.1'), ('001', '1'))
        self.assertTupleEqual(icd9.decimal_to_parts('9.9'), ('009', '9'))

    def test_one_zero_padded_major_one_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('001.1'), ('001', '1'))

    def test_two_major_two_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('22.22'), ('022', '22'))
        self.assertTupleEqual(icd9.decimal_to_parts('88.88'), ('088', '88'))

    def test_two_zero_padded_major_two_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('022.22'), ('022', '22'))

    def test_three_major_one_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('333.3'), ('333', '3'))
        self.assertTupleEqual(icd9.decimal_to_parts('777.6'), ('777', '6'))

    def test_three_major_no_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('444'), ('444', ''))

    def test_three_major_zero_padded_one_minor(self):
        self.assertTupleEqual(icd9.decimal_to_parts('009.9'), ('009', '9'))



class ShortToDecimalTestCase(TestCase):

    def test_one_zero_padded_major(self):
        self.assertEqual(icd9.short_to_decimal('001'), '1')

    def test_one_zero_padded_major_one_minor(self):
        self.assertEqual(icd9.short_to_decimal('0010'), '1.0')
        self.assertEqual(icd9.short_to_decimal('0011'), '1.1')

    def test_one_zero_padded_major_two_minor(self):
        self.assertEqual(icd9.short_to_decimal('00123'), '1.23')

    def test_two_zero_padded_major(self):
        self.assertEqual(icd9.short_to_decimal('022'), '22')
        self.assertEqual(icd9.short_to_decimal('081'), '81')

    def test_two_zero_padded_major_one_minor(self):
        self.assertEqual(icd9.short_to_decimal('0811'), '81.1')

    def test_two_zero_padded_major_two_minor(self):
        self.assertEqual(icd9.short_to_decimal('08123'), '81.23')

    def test_three_major(self):
        self.assertEqual(icd9.short_to_decimal('345'), '345')
        self.assertEqual(icd9.short_to_decimal('991'), '991')

    def test_three_major_one_minor(self):
        self.assertEqual(icd9.short_to_decimal('9911'), '991.1')

    def test_three_major_two_minor(self):
        self.assertEqual(icd9.short_to_decimal('99123'), '991.23')

    def test_vcode_major_one_minor(self):
        self.assertEqual(icd9.short_to_decimal('V013'), 'V01.3')


class ShortToPartsTestCase(TestCase):

    def test_ecode_major_no_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E100'), ('E100', ''))

    def test_one_zero_ecodeno_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E0'), ('E000', ''))

    def test_two_zeros_ecode_major_no_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E00'), ('E000', ''))

    def test_three_zeros_ecode_major_no_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E000'), ('E000', ''))

    def test_one_ecode_zero_padded_major_no_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E1'), ('E001', ''))

    def test_three_ecode_zero_padded_major_no_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E001'), ('E001', ''))

    def test_three_ecode_zero_padded_major_one_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E0123'), ('E012', '3'))

    def test_three_ecode_major_one_minor(self):
        self.assertTupleEqual(icd9.short_to_parts('E1234'), ('E123', '4'))


class PartsToDecimalTestCase(TestCase):

    def test_one_zero_major_no_minor(self):
        self.assertEqual(icd9.parts_to_decimal('0', ''), '0')

    def test_many_zeros_major_no_minor(self):
        self.assertEqual(icd9.parts_to_decimal('000', ''), '0')

    def test_one_zero_padded_major_one_minor(self):
        self.assertEqual(icd9.parts_to_decimal('001', '1'), '1.1')
        self.assertEqual(icd9.parts_to_decimal('009', '9'), '9.9')

    def test_one_zero_padded_vcode_major_one_minor(self):
        self.assertEqual(icd9.parts_to_decimal('V01', '2'), 'V1.2')

    def test_two_zero_padded_major_two_minor(self):
        self.assertEqual(icd9.parts_to_decimal('022', '22'), '22.22')
        self.assertEqual(icd9.parts_to_decimal('088', '88'), '88.88')

    def test_three_major_no_minor(self):
        self.assertEqual(icd9.parts_to_decimal('444', ''), '444')

    def test_three_major_one_minor(self):
        self.assertEqual(icd9.parts_to_decimal('333', '3'), '333.3')
        self.assertEqual(icd9.parts_to_decimal('777', '6'), '777.6')


class PartsToShortTestCase(TestCase):

    def test_one_zero_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E0', ''), 'E000')

    def test_two_zeros_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E00', ''), 'E000')

    def test_three_zeros_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E000', ''), 'E000')

    def test_one_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E1', ''), 'E001')

    def test_two_zero_padded_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E01', ''), 'E001')

    def test_three_zero_padded_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E001', ''), 'E001')

    def test_three_ecode_major_no_minor(self):
        self.assertEqual(icd9.parts_to_short('E100', ''), 'E100')

    def test_three_zero_padded_ecode_major_one_minor(self):
        self.assertEqual(icd9.parts_to_short('E012', '3'), 'E0123')

    def test_three_ecode_major_one_minor(self):
        self.assertEqual(icd9.parts_to_short('E123', '4'), 'E1234')

    def test_one_vcode_major_one_zero_minor(self):
        self.assertEqual(icd9.parts_to_short('V1', '0'), 'V010')

    def test_one_vcode_major_one_minor(self):
        self.assertEqual(icd9.parts_to_short('V1', '1'), 'V011')

    def test_two_vcode_major_one_zero_minor(self):
        self.assertEqual(icd9.parts_to_short('V01', '0'), 'V010')

    def test_two_vcode_major_one_minor(self):
        self.assertEqual(icd9.parts_to_short('V01', '1'), 'V011')


decimal_to_short_suite = TestLoader().loadTestsFromTestCase(DecimalToShortTestCase)
decimal_to_parts_suite = TestLoader().loadTestsFromTestCase(DecimalToPartsTestCase)
short_to_decimal_suite = TestLoader().loadTestsFromTestCase(ShortToDecimalTestCase)
short_to_parts_suite = TestLoader().loadTestsFromTestCase(ShortToPartsTestCase)
parts_to_decimal_suite = TestLoader().loadTestsFromTestCase(PartsToDecimalTestCase)
parts_to_short_suite = TestLoader().loadTestsFromTestCase(PartsToShortTestCase)

all_convert_tests = TestSuite([
    decimal_to_short_suite,
    decimal_to_parts_suite,
    short_to_decimal_suite,
    short_to_parts_suite,
    parts_to_decimal_suite,
    parts_to_short_suite
])

