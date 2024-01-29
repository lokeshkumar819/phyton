#wap that accepts a sentences and calculate the number of space
#   and digit 

sentence=input('enter a sentence')
space=0
digit=0
for char in sentence:
    if char .isspace():
        space+=1
    elif char .isdigit():
        digit+=1
print("SPACE",space)
print("DIGIT",digit)



