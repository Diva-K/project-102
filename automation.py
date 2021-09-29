f=open("test.txt")
file_lines=f.readlines()
for line in file_lines:
    print(line)
found=False
search_string=input("enter the word you want to search")
input_string=input("enter your string")
words=input_string.split()
for word in words:
    if word == search_string:
        found=True
if found==True:
    print("word found")
else:
    print("word not found")