class utils:
    def reversed (num: int):
        # Check for faulty inputs
        if not isinstance(num, int):
                    raise TypeError(f"Expected int, but got {type(num).__name__}")
        
        # Empty list to keep digits 
        digits = []

        # Add digits to digits list while dividing by 10
        while (num >= 1):
            digit = num%10
            digits.append(digit)
            num = int(num/10)

        res = 0

        for i in range (len(digits)):
            res = res + digits[len(digits) - 1 - i]*(10**i)

        return res

    def formatter (num: int):
        # Check for faulty inputs
        if not isinstance(num, int):
                    raise TypeError(f"Expected int, but got {type(num).__name__}")

        bin_num = bin(num)
        oct_num = oct(num) 

        return bin_num, oct_num