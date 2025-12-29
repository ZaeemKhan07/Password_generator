import unittest
# Ensure this import matches your actual main file name (e.g. 'main')
from main import generate_password, letters, numbers, symbols

class TestPyPasswordGenerator(unittest.TestCase):

    def test_total_length(self):
        """Test 1: Check if the generated password has the correct total length."""
        n_letters = 4
        n_symbols = 3
        n_numbers = 2
        total_expected = n_letters + n_symbols + n_numbers
        
        result = generate_password(n_letters, n_symbols, n_numbers)
        
        # --- NEW: Print the actual output ---
        print(f"\n[Test 1] Input: 4 Letters, 3 Symbols, 2 Numbers -> Result: {result}")
        
        self.assertEqual(len(result), total_expected, 
                         f"Expected password length {total_expected}, but got {len(result)}")

    def test_content_count(self):
        """Test 2: Check if the password contains the exact number of specific types requested."""
        n_letters = 2
        n_symbols = 2
        n_numbers = 2
        
        result = generate_password(n_letters, n_symbols, n_numbers)
        
        # --- NEW: Print the actual output ---
        print(f"\n[Test 2] Input: 2 Letters, 2 Symbols, 2 Numbers -> Result: {result}")
        
        # Count items in the result
        count_l = sum(1 for char in result if char in letters)
        count_s = sum(1 for char in result if char in symbols)
        count_n = sum(1 for char in result if char in numbers)
        
        self.assertEqual(count_l, n_letters, "Letter count mismatch")
        self.assertEqual(count_s, n_symbols, "Symbol count mismatch")
        self.assertEqual(count_n, n_numbers, "Number count mismatch")

    def test_zero_inputs(self):
        """Test 3: Check if passing zeros returns an empty string."""
        result = generate_password(0, 0, 0)
        
        # --- NEW: Print the actual output ---
        print(f"\n[Test 3] Input: 0, 0, 0 -> Result: '{result}'")
        
        self.assertEqual(result, "", "Should return an empty string when inputs are 0")

if __name__ == '__main__':
    unittest.main()
