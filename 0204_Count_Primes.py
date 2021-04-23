""" Math """


class Solution:
    def countPrimes(self, n: int) -> int:
        prime = []
        is_prime = [True] * n
        for i in range(2, n):
            if is_prime[i]:
                prime.append(i)
            for j in prime:
                if j * i >= n:
                    break
                is_prime[i * j] = False
                if not i % j:
                    break
        return len(prime)


print(Solution().countPrimes(n=10))
