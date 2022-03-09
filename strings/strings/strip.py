#strip() removes all the leading and trailing spaces from a str
s="  devika is so cool   "
s=s.strip()
print(s) #devika is so cool

name="devu.maya."
name=name.strip('.')  #strip only removes speified chara that is either leading or trailing
print(name) #devika.maya