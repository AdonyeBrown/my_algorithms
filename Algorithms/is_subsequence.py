class IsSubSequence:
    def isSubsequence(self, substring: str, string: str) -> bool:
        sub_str = len(substring)
        super_str = len(string)
        # An empty string is always a substring of a string
        if substring == "":
            return True
        # check if substring is longer than string
        if sub_str > super_str:
            return False

        j = 0  # for the index of the substtring
        for i in range(super_str):
            # check if both string and substring char are the same
            if string[i] == substring[j]:
                # check if we have got to the endof the substring
                if j == sub_str-1:
                    return True
                j += 1  # increment j

        return False


iss = IsSubSequence()
print(iss.isSubsequence("ode", "russeladonye"))
print(iss.isSubsequence("ado", "russeladonye"))
print(iss.isSubsequence("on", "russeladonye"))
print(iss.isSubsequence("us", "russeladonye"))
print(iss.isSubsequence("onye", "russeladonye"))
