class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # Initialize list to build the result string parts
        res_parts = []

        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            res_parts.append("-")

        # Use absolute values for calculation
        N = abs(numerator)
        D = abs(denominator)

        # Append the integer part
        res_parts.append(str(N // D))
        remainder = N % D

        # If there's no remainder, return the integer part
        if remainder == 0:
            return "".join(res_parts)

        # Append the decimal point
        res_parts.append(".")

        # Store remainders and their corresponding index in `decimal_digits`
        # This map helps detect repeating cycles: remainder -> index of its corresponding digit
        remainder_map = {}
        decimal_digits = [] # List to store digits of the fractional part

        # Generate fractional part digits
        while remainder != 0:
            if remainder in remainder_map:
                # Cycle detected!
                repeat_start_idx = remainder_map[remainder]

                # Append the non-repeating part of decimal_digits to res_parts
                for i in range(repeat_start_idx):
                    res_parts.append(decimal_digits[i])

                # Append the opening parenthesis
                res_parts.append("(")

                # Append the repeating part of decimal_digits to res_parts
                for i in range(repeat_start_idx, len(decimal_digits)):
                    res_parts.append(decimal_digits[i])
                
                # Append the closing parenthesis
                res_parts.append(")")
                
                # Return the final string
                return "".join(res_parts)

            # If remainder not seen before, record its position
            remainder_map[remainder] = len(decimal_digits)

            # Perform the long division step
            remainder *= 10
            digit = remainder // D
            decimal_digits.append(str(digit))
            remainder %= D
        
        # If the loop finishes, it means remainder became 0, so no repeating part
        for digit_char in decimal_digits:
            res_parts.append(digit_char)
            
        return "".join(res_parts)