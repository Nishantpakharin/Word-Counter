fileName = input('Enter the file name: ')
file = open(fileName,'r')

contents = file.read()
# print(contents)

words = contents.split()
num = len(words)
n = len(contents)

print(f"{num} words and {n} characters")
