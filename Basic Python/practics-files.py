# Q1- Check 'Twinkle' is present or not.
'''
with open('poem.txt', 'r') as f:
        a=f.read('Twinkle' == True)
print("Present")        


f = open('poem.txt')
a = f.read()
if 'Twinkle' in a:
    print("'Twinkle' is Present")
else:
    print("Not Present")    
print(a)
f.close()
'''


#Q2- write highscore of a player in highscore book if it greater then earlier player or if notebook is blank 
'''
def game():
    return 668

newscore=game()
with open('highscore.txt','r') as f:
    highscore = (f.read())

if highscore == '':
    with open('highscore.txt','w') as f:
        f.write(str(newscore))

elif newscore>int(highscore):
    with open('highscore.txt','w') as f:
        f.write(str(newscore))

'''


# Q3- Generate a table of 2-20 and write it in dillerent folder. 
# This question is solved in table folder



# Q4 replace word donkey  to #%@&$^%#. 
'''
with open('sample.txt') as f:
    content = f.read()

#if 'Donkey' in content:
content=content.replace('Donkey' , '#$%&^*')  

with open('sample.txt' , 'w') as f:
    content = f.write(content)    

'''




