class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}
        for word in strs:
            prime_prd = self.prime_products(word)
            # freq.setdefault(prime_prd,[]).append(word)

            if prime_prd not in freq:
                freq[prime_prd] = [word]
            else:
                freq[prime_prd].append(word)
            
        return list(freq.values())
        

    def prime_products(self, word):
        prime_prd = 1
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for ch in word:
            prime_prd *= primes[ord(ch) - ord('a')]

        return prime_prd

