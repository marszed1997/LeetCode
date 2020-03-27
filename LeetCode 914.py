class Solution:

    def __init__(self):
        self.Count = {}

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a%b)

    def hasGroupsSizeX(self, deck) -> bool:
        """
        :param deck: List[int]
        :return: bool
        """
        for i in deck:
            if i in self.Count:
                self.Count[i] += 1
            else:
                self.Count[i] = 1
        ans = 0
        for id, value in enumerate(self.Count.values()):
            if id == 0:
                ans = value
            ans = self.gcd(ans, value)
            if ans <= 1:
                return False
        return True