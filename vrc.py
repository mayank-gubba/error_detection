"""CODE BY MAYANK GUBBA
for finding errors using LRC and VRC
menu driven code for selecting and finding errors"""
def vrc_sender(sender):
    sender=str(sender) #converting the input into a string 
    c1=sender.count('1') #counting the number of 1's
    #adding even parity based on number of 1's
    if c1%2==0:
        receiver=sender+str(0)
    elif c1%2!=0:
        receiver=sender+str(1)
    return receiver

def vrc_receiver(receiver,received):
    received=str(received)
    c1=received.count('1')
    #checking number of 1's in received data
    if c1%2==0:
        if received==receiver:
            print('correct data received')
        elif received!=receiver: #if two bits received wrong then the parity may remain same
            print('wrong data accepted')
    elif c1%2==1:
        print('wrong data discard')


#lrc encoding done
def lrc_sender():
    a=list(map(str,input('enter the data blocks: ').split()))
    sender=[]
    #adding row parity
    for i in a:
        temp=vrc_sender(i)
        sender.append(list(str(temp)))
    n=len(sender[0])
    check=[] #array to store column parity
    #adding column parity by accesing one column at a time
    for i in range(n):
        col=[row[i] for row in sender]
        col=''.join(col)
        c=vrc_sender(col)
        c=c[-1]
        check.append(c)
    encode=sender.copy()
    encode.append(check)
    print('encoded data is: ',[''.join(i) for i in encode])
    return [''.join(i) for i in encode]

#lrc decoding to be done
def lrc_receiver(sender):
    b=list(map(str,input('enter the received data blocks: ').split()))
    n=len(b[0])
    e=0#checking the total number of bits effected
    for i in range(n):#checking the error in column parity bits
        coll=[row[i] for row in b]
        coll=''.join(coll)
        if coll.count('1')%2!=0:
                print('wrong data in column',i+1)
                e+=1
    for j in range(len(b)):#checking for error in row parity bits
        if b[j].count('1')%2!=0:
            print('wrong data received at row',j+1)
            e+=1
    if e==0:#if four bits are changed there is not chnge in parity bits
        if b==sender:#comparing recevier data and sender data
            print('correct data received')
        elif b!=sender:
            print('wrong data accepted')


run=True
while run==True:
    t=int(input('\nENTER 1 FOR VRC\n2 FOR LRC\n3 QUIT:\n'))
    if t==1:
        i=input('enter string to be sent: ')
        d=vrc_sender(i)
        print('using even bit parity the encoded data is:\n',d)
        r=int(input('enter received data: '))
        vrc_receiver(d,r)
    elif t==2:
        d=lrc_sender()
        lrc_receiver(d)
    elif t==3:
        print('THANK YOU')
        run=False
    else:
        print('CHOOSE A CORRECT VALUE')

print("testing")