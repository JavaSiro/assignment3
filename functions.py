#b
# def calculator(first,second):
#     print(f'addition is {first+second}')
#     print(f'subtraction is {first-second}')
# first=int(input('type in the first number: '))
# second=int(input('type in the second number: '))
# calculator(first,second)

#c
# def calculator():
#     num = 0
#     for i in range(1, 11):
#         num += i
#     return num
# print(calculator())

#d
# def work():
#     list=[]
#     for i in range(50,101):
#         if i%2==0:
#             list.append(i)
#     return list
# print(work())

#e
# def detector(num):
#     if num%2==0:
#         return f'{num}' ' is even'
#     elif not num%2==0:
#         return f'{num}' ' is odd'
#     else:
#         return f'{num}' ' is 0'
# num=int(input('type in ur number '))
# print(detector(num))

#f
# text=str(input('type: '))
# def reverse_string(text):
#     reversed_string = text[::-1]
#     print(reversed_string)
# reverse_string(text)

#g
# def abc(num):
#     print(chr(num))
# raqam = int(input("Key num: "))
# abc(num)

#h
# def detect():
#     return max(list(range(1,2001)))
# print(detect())

#i
# def detector(age):

#     return 2025-age
# clientage=int(input('type ur birth year'))
# print(detector(clientage))

#j
# def converter(num):
#     return abs(num)
# num = int(input("type negative: "))
# print(converter(num))

#k
# def converter(text):
#     print(text.upper())
# client=str(input('type: '))
# converter(client)

#l
# def a(students, name):
#     if name in students:
#         print('isso')
#     else: print('opso')
# students=['java', 'fedya', 'mira', 'aziz', 'adam']
# name=str(input('type name'))
# a(students, name)

#m
# def a(students):
#     updated=[]
#     for i in students:
#         if len(i)>5:
#             updated.append(i)
#     return updated
# students=['java', 'fedya', 'mira', 'aziz', 'adam']
# print(a(students))

#n
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count

# input_text = input("Enter a string: ")
# print(f"The number of vowels in the string is: {count_vowels(input_text)}")

#o
# def sum(list): return [(data ** 2 + data ** 3) for data in list]
# def sum(list):
#     for i in range(0, len(list)):
#         list[i] = list[i] ** 2 + list[i] ** 3
#     return list

# list = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10]
# print(sum(list))

#p
# def text(list):
#     max = ""
#     for i in list:
#         if len(i) > len(max): max = i
#     return max

# list = ['java', 'javohir', 'python']
# print(text(list))

#q
# def letter(str):
#     l = len(str)
#     if l % 2 == 1:
#         print(str[l // 2])
#     else: 
#         print(str[l // 2 - 1] + str[l // 2])

# txt = input("type: ")
# letter(txt)