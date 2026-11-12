def two_sum(nums, target):
    # Outline:
    # Find two numbers that add up to target.
    # Use a dictionary to remember numbers and their indices.
    # Check if the needed number has already appeared.

    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]

        seen[nums[i]] = i


def max_profit(prices):
    # Outline:
    # Keep track of the lowest price.
    # Calculate the profit for each day.
    # Return the highest profit.

    lowest = prices[0]
    best_profit = 0

    for price in prices:
        profit = price - lowest

        if profit > best_profit:
            best_profit = profit

        if price < lowest:
            lowest = price

    return best_profit


def max_subarray(nums):
    # Outline:
    # Keep track of the current sum and largest sum.
    # Start a new group if the current number is better alone.
    # Return the largest sum.

    current = nums[0]
    largest = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        largest = max(largest, current)

    return largest


def is_balanced(s):
    # Outline:
    # Use a stack to remember opening brackets.
    # Check that each closing bracket matches.
    # Return True if all brackets are closed correctly.

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def main():
    print(two_sum([2, 7, 11, 15], 9))
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(is_balanced("{[]}"))


if __name__ == "__main__":
    main()
