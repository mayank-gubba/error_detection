"""CODE BY MAYANK GUBBA
for encoding and decoding a meesage using the CRC technique.
We use the method of binary division for solving this question"""
# A function for doing the bitwise xor between two numbers
def xor(s1,s2):
    ans=''
    for i in range(len(s1)):
        ans+=str(int(s1[i])^int(s2[i]))
    return ans
# A function for doing binary division
def gcrc(m,d):
    if m[0]=='1': #first iteration of division is done outside the for loop
        r=xor(m[:len(d)],d)
    else:
        r=xor('0'*len(d),d)
    temp=r
#this loop brings each digit down and performs binary division with divsor using xor function
    for i in range(len(d),len(m)):
        temp+=m[i]
        temp=temp[-len(d):]
        if temp[0]=='0':
            temp=xor('0'*len(d),temp)
        else:
            temp=xor(temp,d)
    crc=temp[-(len(d)-1):]
    return crc
# a function for encoding the message
def encode(m,d):
    m1=m+'0'*(len(d)-1) #appending the 0's to the message
    e=gcrc(m1,d) #finding the remainder using crc for encoding function
    m=m+e #encoding function by adding crc to the end of messaage before sending it
    print('CRC generated:',e)
    return m
# a function for decoding the message
def decode(m,r,d):
    c=gcrc(r,d)
    if int(c)==0:
        if m==r:
            print('wrong data accepted')
        else:
            print('No error')
            print('extracted data:',r[:-len(c)])
    else:
        print('wrong data discard')

#main driver code taking input for sender and receiver side    
m=input('enter input data:')
dm=input('enter divisor:')
print('encoded data',encode(m,dm))

r=input('enter received data:')
dr=input('enter divisor:')
decode(m,r,dr)
