class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp = n
        for i in range(len(flowerbed)):

            if (
                (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                and 0 == flowerbed[i]
            ):
                flowerbed[i] = 1
                tmp -= 1
        return tmp <= 0
