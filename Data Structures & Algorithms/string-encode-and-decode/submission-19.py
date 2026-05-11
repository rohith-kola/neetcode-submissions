class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "/" + word
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 0:
            return []
        position = 0
        words = []
        while position < len(s):
            length = ""
            while s[position] != "/":
                length += s[position]
                position += 1
            length = int(length)
            words.append(s[position + 1: position + 1 + length])
            position = position + 1 + length
        return words