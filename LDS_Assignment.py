# Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    num_count = {}

    for num in arr:
        complement = target_sum - num
        if complement in num_count and num_count[complement] > 0:
            pairs.append((num, complement))
            num_count[complement] -= 1
        else:
            num_count[num] = num_count.get(num, 0) + 1

    return pairs

if __name__ == "__main__":
    input_array = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
    target_sum = 7
    result_pairs = find_pairs_with_sum(input_array, target_sum)

    if result_pairs:
        print(f"Pairs with sum {target_sum}:")
        for pair in result_pairs:
            print(pair)
    else:
        print(f"No pairs found with sum {target_sum}.")
# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.



def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5]
    print("Original Array:", input_array)
    
    reverse_array_in_place(input_array)

    print("Reversed Array:", input_array)

# Write a program to check if two strings are a rotation of each other?

def are_strings_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated_str = str1 + str1
    if str2 in concatenated_str:
        return True
    else:
        return False

if __name__ == "__main__":
    str1 = "abcd"
    str2 = "cdab"
    if are_strings_rotations(str1, str2):
        print(f"'{str1}' and '{str2}' are rotations of each other.")
    else:
        print(f"'{str1}' and '{str2}' are not rotations of each other.")

# Write a program to print the first non-repeated character from a string?

def first_non_repeated_char(s):
    char_freq = {}

    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    for char in s:
        if char_freq[char] == 1:
            return char
    return None
if __name__ == "__main__":
    input_string = "hello"
    result = first_non_repeated_char(input_string)

    if result:
        print(f"The first non-repeated character in '{input_string}' is '{result}'.")
    else:
        print(f"There are no non-repeated characters in '{input_string}'.")

# Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    num_disks = 3
    tower_of_hanoi(num_disks, 'A', 'B', 'C')

# Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def postfix_to_prefix(postfix_expr):
    stack = []

    for char in postfix_expr.split():
        if is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)
        else:
            stack.append(char)
    return stack.pop()

if __name__ == "__main__":
    postfix_expr = "3 5 2 * +"
    prefix_expr = postfix_to_prefix(postfix_expr)
    print("Postfix expression:", postfix_expr)
    print("Prefix expression:", prefix_expr)

# Write a program to convert prefix expression to infix expression.

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(prefix_expr):
    stack = []

    for char in reversed(prefix_expr.split()):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1} {char} {operand2})")
        else:
            stack.append(char)

    return stack.pop()

if __name__ == "__main__":
    prefix_expr = "+ * 3 5 2"
    infix_expr = prefix_to_infix(prefix_expr)
    print("Prefix expression:", prefix_expr)
    print("Infix expression:", infix_expr)

# Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_closed(code):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in code:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or bracket_pairs[char] != stack.pop():
                return False

    return len(stack) == 0

if __name__ == "__main__":
    code_snippet1 = "{(a + b) * [c - d]}"
    code_snippet2 = "if (a > b) {print('Hello!')"
    
    if are_brackets_closed(code_snippet1):
        print("Code snippet 1: All brackets are closed.")
    else:
        print("Code snippet 1: Brackets are not closed properly.")
    
    if are_brackets_closed(code_snippet2):
        print("Code snippet 2: All brackets are closed.")
    else:
        print("Code snippet 2: Brackets are not closed properly.")

# Write a program to reverse a stack.


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty():
        temp_stack.push(stack.pop())

    return temp_stack

if __name__ == "__main__":
    original_stack = Stack()
    original_stack.push(1)
    original_stack.push(2)
    original_stack.push(3)
    original_stack.push(4)

    print("Original Stack:", original_stack.items)

    reversed_stack = reverse_stack(original_stack)

    print("Reversed Stack:", reversed_stack.items)
    
#Write a program to find the smallest number using a stack.


class Stack:
    def __init__(self):
        self.items = []
        self.min_value = None

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.min_value is None or item < self.min_value:
            self.min_value = item
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_min(self):
        return self.min_value

if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(1)

    print("Stack:", stack.items)
    print("Smallest number in the stack:", stack.get_min())
