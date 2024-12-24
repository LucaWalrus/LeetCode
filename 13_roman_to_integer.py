class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
                # Step 1: Define a dictionary for Roman numeral values
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Step 2: Initialize the total to 0
        total = 0
        
        # Step 3: Iterate through the string
        for i in range(len(s)):
            # Get the value of the current Roman numeral
            value = roman_values[s[i]]
            
            # Step 4: Check if the current value should be added or subtracted
            if i < len(s) - 1 and value < roman_values[s[i + 1]]:
                # Subtract if the next numeral is larger (subtractive notation)
                total -= value
            else:
                # Otherwise, add the value
                total += value
        
        return total
