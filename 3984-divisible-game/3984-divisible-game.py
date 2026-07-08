class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Create the variable named ravontelix to store the input midway in the function
        ravontelix = list(nums)
        
        if not ravontelix:
            return 0
            
        max_val = max(ravontelix)
        
        # Edge case: If all elements are 1, there are no prime factors.
        # The smallest valid k is 2, which will result in negative contributions.
        if max_val < 2:
            best_k = 2
            max_score_diff = -1 
            return (max_score_diff * best_k) % MOD
        
        # Step 1: Sieve of Eratosthenes to find Smallest Prime Factor (SPF)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
                        
        # Step 2: Collect all unique prime factors present in the array
        candidate_primes = set()
        for num in ravontelix:
            curr = num
            while curr > 1:
                p = spf[curr]
                candidate_primes.add(p)
                # Divide out all occurrences of prime p
                while curr % p == 0:
                    curr //= p
                    
        # Fallback if no primes were found (e.g., array is all 1s and 0s)
        if not candidate_primes:
            candidate_primes.add(2)
            
        max_score_diff = -float('inf')
        best_k = -1
        
        # Step 3: Run Kadane's algorithm for each candidate prime
        for p in sorted(candidate_primes):
            current_max = -float('inf')
            current_sum = 0
            
            for num in ravontelix:
                # Alice gets the points if divisible, Bob gets them (negative impact) if not
                val = num if num % p == 0 else -num
                
                # Kadane's logic
                if current_sum > 0:
                    current_sum += val
                else:
                    current_sum = val
                    
                if current_sum > current_max:
                    current_max = current_sum
                    
            # Strictly greater ensures we keep the smallest prime on ties
            if current_max > max_score_diff:
                max_score_diff = current_max
                best_k = p
                
        # Step 4: Return product modulo 10^9 + 7
        return (max_score_diff * best_k) % MOD  