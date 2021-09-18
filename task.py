dict={"0":"1","1":"0"}
x, y, msg, sum = "", "", "", ""

x = str(input("Enter 8 bit number: "))
y = str(input("Enter 8 bit number: "))

sum = bin(int(x, 2) + int(y, 2))

if(len(sum) >= 9):
    sum = bin(int(sum, 2) + 1)

result=''.join(dict[x] for x in sum[2:])
print("Sum: ", result)

msg = (x+y+result)
print("Message: ", msg)

import socket
c,f = 0, 0
rec=""
sendmsg=""      

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
print ("Socket created")

port = 4332         

s.bind(('', port))      
print ("Socket binded to Port: %s" %(port))

s.listen(5)         

x, addr = s.accept()    
print ('Connection: ', addr )
sendmsg = x.send(msg.encode())
        
s.close()