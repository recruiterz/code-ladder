class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)

        def recursive(piles, is_alex_turn, alex_sc):
            if not piles:
                return True if alex_sc > total - alex_sc else False
            return recursive(piles[1:], not is_alex_turn, alex_sc + piles[0]) or recursive(piles[:-1], not is_alex_turn, alex_sc + piles[-1])
        return recursive(piles, True, 0)
