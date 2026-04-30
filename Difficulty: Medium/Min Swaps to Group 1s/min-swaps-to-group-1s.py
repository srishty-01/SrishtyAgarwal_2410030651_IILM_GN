class Solution:
    def minSwaps(self, arr):
        total_ones = sum(arr)

        # If no 1s present
        if total_ones == 0:
            return -1

        # Count zeros in first window
        zeros = arr[:total_ones].count(0)
        min_swaps = zeros

        # Sliding window
        for i in range(total_ones, len(arr)):
            if arr[i - total_ones] == 0:
                zeros -= 1
            if arr[i] == 0:
                zeros += 1

            min_swaps = min(min_swaps, zeros)

        return min_swaps