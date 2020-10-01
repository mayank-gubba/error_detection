"""CODE BY MAYANK GUBBA
for demonstrating byte and bit and byte stuffing and unstuffing
here the flag and escape character can be given as input"""

s=input("enter your string here: ")
flag=input("enter flag symbol: ")
esc=input("enter esc symbol: ")
#entering a flag at the beginning of string for byte stuffing
byte_stuff=flag+""
#entering each charcter of string with escape character before flag character
for i in s:
    if i==flag:
       byte_stuff+=esc
    byte_stuff+=i
byte_stuff+=flag
print("after byte stuffing: ",byte_stuff)
byte_unstuff=""
flag_check=False #a counter to mark starting and end of data
for i in range(len(byte_stuff)):
    if flag_check==False: #checking for first flag in the data received
        if byte_stuff[i]== flag:
            flag_check=True
    elif flag_check==True:
        #flag encountered checking if there is escape character before it and adding the flag to decoded data
        if byte_stuff[i]==flag: 
            if byte_stuff[i-1]==esc:
                byte_unstuff+=byte_stuff[i]
            #if flag encountered without escape character mark it as end of data and stop transmission
            else: 
                flag_check=False
                break
        elif byte_stuff[i]!=esc:
            byte_unstuff+=byte_stuff[i]

print("after byte unstuffing: ",byte_unstuff)

#Bit stuffing and unstuffing below
b=input("enter your string here: ")
flag="01111110"
r=""
for i in b:#converting the input string into binary format
    r+="{0:b}".format(ord(i))
print("string in binary: ",r)
count=0
sender=""
sender+=flag #adding flag at begining of the binary string
for i in r: 
    sender+=i
    if i=='1':
        count+=1
        if count==5: #adding zero in the string after consecutive 5 1's
            sender+='0'
    if i=='0':
        count=0
    
sender+=flag
print("bit stuffing: ",sender)

check,count=False,0
try:
    for i in range(len(sender)):
        if (sender[i:i+8]==flag):#checking for the first flag in data
            sender=sender.replace(flag,"",1)
            check=True
        if check==True:
            if sender[i]=='1':
                count+=1
                if count==5: #removing the zero that occurs after 5 consecutive 1's
                    sender=sender[:(i+1)]+sender[(i+2):]
            if sender[i]=='0':
                count=0

except IndexError:
    pass
print("bit unstuffing: ",sender)
