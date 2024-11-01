# qus-2

s=input()
t=s[len(s)-3::]
print(t)
if t=="ing":
    s.replace(s[len(s)-3::],"ly")
else:
    s=s+"ing"
print(s)
