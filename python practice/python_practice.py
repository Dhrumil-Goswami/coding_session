# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result =[]
#         for i in nums1:
#         	print i
#         	for j in num1

# solution = Solution()
# print(solution.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
# # print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9] or [9, 4] depending on the order of intersection


# [2,4,6,7,3,8,1]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for index, val in enumarate(nums):
#             complement = target - val
#             if complement in nums:
#                 return [val, complement]

# # Test Input
# nums = [2, 7, 11, 15]
# target = 9

# # Expected Output: [0, 1]
# solution = Solution()
# print(solution.twoSum(nums, target))
# import itertools


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Function to print linked list
# def list_node(l):
#     current = l
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")

# # Create linked lists
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))

# # Print linked lists
# print("List 1:")
# list_node(l1)

# print("\nList 2:")
# list_node(l2)




# print(max(4, 3))
# s = "pwwkew"
# res = []
# cnt = 0
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         if s[j] not in res:
#             res.append(s[j])
#             if len(res) > cnt:
#                 cnt  = len(res)
#         else:
#             res.clear()
#             break

# print(res)
        
# print("\n\n\n::::::::cnt", cnt)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()  # A set to keep track of characters in the current window
#         left = 0  # Left pointer for the sliding window
#         max_length = 0  # To keep track of the maximum length found
        
#         for right in range(len(s)):
#             # If the character at 'right' is already in the set, remove characters from the left until it's not
#             print("\n\n\n::::leftbefore", left)
#             print("\n\n\n::::s[right]", s[right])
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
            
#             print("\n\n\n::::left", left)
#             # Add the character at 'right' to the set
#             char_set.add(s[right])
#             print("\n\n\n::::char_set", char_set)
            
#             # Update the maximum length
#             max_length = max(max_length, right - left + 1)
#             print("\n\n\n::::max_length", max_length)
        
#         return max_length

# # Example usage:
# import collections

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         q = deque()
#         for c in s:
#             if c in q:
#                 prnt("\n\nbefore while", c)
#                 while q.popleft() != c:
#                     print ("\n\n\nwhile c", c)

#                     pass
#             q.append(c)
#             res = max(res, len(q))
        
#         return res

# solution = Solution()
# print(solution.lengthOfLongestSubstring("dvdf"))  # Output: 3



# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if int(year) % 4 == 0 and int(year) > 1:
#         if (int(year) % 100 == 0) and (int(year) % 400 == 0):
#             leap = True
#         else:
#             leap = False
#     return leap

# print(is_leap(2000))
# import array
# arr = array.array('i', [1,2,3,4])
# arr.append(5)
# arr.pop(1)
# arr.remove(4)
# print(arr)

# def sort_list(n):
# 	for i in range (0,len(n)):
# 		min_idx = i
# 		for j in range(i+1, len(n)):
# 			if n[j] < n[min_idx]:
# 				min_idx = j
# 		n[i], n[min_idx] = n[min_idx], n[i]
# 	return n[-2]
# def quick_sort(n):
# 		if len(n) <= 1:
# 			return n
# 		if len(n) > 1:
# 			print(n)
# 			pivot = n[len(n)//2]
# 			left = [x for x in n if x < pivot]
# 			right = [x for x in n if x > pivot]
# 			middle = [x for x in n if x == pivot]
# 			print("l", left)
# 			print("r", right)
# 			print("p", middle)
# 			return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort(n=[80,60,10,70,15,20,100]))

# n = [2,3,4,5] + [] + [10,20] 

# print(n)
# def fact(n):
# 	if n < 0:
# 		return False
# 	return n * fact(n-1) if n > 1 else 1

# print(fact(4))