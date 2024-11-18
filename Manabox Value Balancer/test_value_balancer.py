import unittest
from value_balancer import CSVProcessor

class TestCSVProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = CSVProcessor(input_file='dummy_input.csv', output_file='dummy_output.csv', total_purchase_price=100.0)

    def test_modify_data(self):
        data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "10", "3"],
            ["Item2", "20", "1"],
            ["Item3", "invalid", "3"]
        ]
        expected_data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "20", "3"],
            ["Item2", "40", "1"],
            ["Item3", "0", "3"]
        ]
        modified_data = self.processor.modify_data(data)
        self.assertEqual(modified_data, expected_data)

    def test_modify_data_with_zero_total(self):
        self.processor.total_purchase_price = 0.0
        data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "10", "3"],
            ["Item2", "20", "1"]
        ]
        expected_data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "0", "3"],
            ["Item2", "0", "1"]
        ]
        modified_data = self.processor.modify_data(data)
        self.assertEqual(modified_data, expected_data)

    def test_modify_data_with_all_invalid_prices(self):
        data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "invalid", "3"],
            ["Item2", "invalid", "1"]
        ]
        expected_data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "0", "3"],
            ["Item2", "0", "1"]
        ]
        modified_data = self.processor.modify_data(data)
        self.assertEqual(modified_data, expected_data)

    def test_modify_data_complex_case(self):
        self.processor.total_purchase_price = 200.0
        data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "10.50", "2"],
            ["Item2", "15.75", "3"],
            ["Item3", "25.25", "1"],
            ["Item4", "invalid", "4"],
            ["Item5", "5.50", "5"]
        ]
        expected_data = [
            ["Name", "Purchase price", "Quantity"],
            ["Item1", "17.36", "2"],
            ["Item2", "26.03", "3"],
            ["Item3", "41.74", "1"],
            ["Item4", "0", "4"],
            ["Item5", "9.09", "5"]
        ]
        modified_data = self.processor.modify_data(data)
        self.assertEqual(modified_data, expected_data)

if __name__ == '__main__':
    unittest.main()