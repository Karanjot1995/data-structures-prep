class Solution:
    '''
    APPROACH: Long division
    - Video: https://www.youtube.com/watch?v=2cRS9dNa780&ab_channel=Pepcoding

    TC - O(denominator)
    SC - O(denominator); remainder is always [0, denominator-1] due to modulus operator so hashmap will have at most O(den)

    The loop that processes the decimal part of the number runs until either the remainder becomes zero or a repeating pattern is detected. In the worst case, where there is no repeating pattern, this loop will run at most den times.
    '''
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0: return "-1"

        if numerator == 0: return "0"
        
        ans = []
        sign = "" if numerator * denominator >= 0 else "-"

        if sign: ans.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        quotient = numerator // denominator
        remainder = numerator % denominator
        ans.append(str(quotient))

        if remainder == 0: return "".join(ans)
        else: ans.append(".")
        
        hmap = {} # remainder: index i
        while remainder != 0:
            if remainder in hmap:
                # remainder repeating
                pos = hmap[remainder]
                ans.insert(pos, "(")
                ans.append(")")
                break
            else:
                hmap[remainder] = len(ans)
                remainder *= 10
                quotient = remainder // denominator
                remainder = remainder % denominator
                ans.append(str(quotient))

        return "".join(ans)

s = Solution()
print(s.fractionToDecimal(1, 0))
print(s.fractionToDecimal(1, 2))
print(s.fractionToDecimal(1, 3))
print(s.fractionToDecimal(1, 56))