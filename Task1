# Make up an algorithm 
# If the entered number is greater than 7, then print “Hello” 

def HelloGreater(num):
	if num > 7:
		print('Hello')
	else:
		print('Incorrect number')

#tests
print('Task1.1')
HelloGreater(3) # Incorrect number
HelloGreater(8) # Hello
print()

#If the entered name matches “John”, then output “Hello, John”, if not, then output "There is no such name" 

def HelloJohn(text, *args):
	special_text = 'John'
	if text == special_text:
		print(f'Hello, {special_text}')
	else:
		print('There is no such name')

#tests
print('Task1.2')
HelloJohn('John') # Hello, John
HelloJohn('Mikhail') # There is no such name
print()

#There is a numeric array at the input, it is necessary to output array elements that are multiples of 3 

def Array3times(nums):
    A = nums.split(", ")
    for i in range(len(A)): 
        A[i] = int(A[i]) * 3
    print(A)
        
#tests
print('Task1.3')
Array3times('1, 2, 3') # [3, 6, 9]
Array3times('3, 4, 5') # [9, 12, 15]
