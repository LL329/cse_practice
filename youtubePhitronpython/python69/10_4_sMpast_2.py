# capitalize())
#titile()
#swapcase()
#csefold() text = 'groB'
# replace()
# count()
#isdigit()
#join()


a = "hello world python"
print(a.capitalize()) # first letter only change
print(a.title()) # Every first letter will be capital
b = "hE iS kIND"
print(b.swapcase()) 
# small letter will be capital & capital will be small
c = "groß"
print(c.casefold()) # more powerful than lower()

x = "honda"
print(x)
# y=x.replace('o', 'e',1)
y = x.replace(x[1],'e',1)
print(y)

print(a.count('o'))

p = '999'
print(p.isdigit())

q = ["h", "e", "l", "l", "o"]
r = ["1", "2", "4"]
print("".join(r))
print("".join(q)) #space remover output: Hello
print(q)

# joint() --> list to string
#split() --> list()-->string to list