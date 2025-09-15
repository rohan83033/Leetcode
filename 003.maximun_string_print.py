class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        mask = 0
        for ch in broken:
            mask |= 1 << (ord(ch) - 97)

        count = 0
        bad = False
        for ch in text + " ":
            if ch == " ":
                count += not bad
                bad = False
            elif mask & (1 << (ord(ch) - 97)):
                bad = True
        return count
