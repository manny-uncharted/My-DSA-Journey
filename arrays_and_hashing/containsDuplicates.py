class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}  # A dictionary to store seen elements

        for num in nums:
            # If the element is already in the dictionary, return True (contains duplicates)
            if num in seen:
                return True
            # Otherwise, add it to the dictionary
            seen[num] = True

        # If no duplicates are found after the loop, return False
        return False