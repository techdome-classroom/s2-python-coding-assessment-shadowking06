class Solution:
    def isValid(self, s: str) -> bool:
        """
        Returns True if the input string is valid, False otherwise.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():  # Open bracket
                stack.append(char)
            elif char in mapping:  # Close bracket
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack