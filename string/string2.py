name = "royal ram"

#flag = name.startswith("r")
flag = name.startswith("r",6)
print("flag = ",flag)

flag = name.endswith("m")
print("flag endswith",flag)

#data ="Hi This Is India"
data = "\n"
print("is title...",data.istitle())
print("is lower...",data.islower())
print("is upper",data.isupper())
print("alpha num",data.isalnum())
print("alpha",data.isalpha())
print("is numric",data.isnumeric())
#print("is decimal..",data.isdecimal())
print("isSpace",data.isspace())
print("isprintable",data.isprintable())

