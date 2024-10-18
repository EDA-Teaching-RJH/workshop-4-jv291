camel = input("input a variable in camel case")
list(camel)
snake = " "
for c in camel:
    if c.isupper():
        snake += "_" +c.lower()
    else:
        snake += c
snake
print (snake)