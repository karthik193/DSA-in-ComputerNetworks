def xor(a,b):
   s= ''
   for i in range(len(a)):
      if(a[i] == b[i]):
         s+='0'
      else:
         s+= '1'
   return s[1:] 
def divide(data , div):
   n = len(data)
   divLen = len(div)
   z = "0"*divLen 
   curr = data[:divLen]
   i = divLen
   if(curr[0] == '1'):
      curr = xor(curr , div)
   else :
      curr = xor(curr, z)
   while(i< n ):
      
      curr += data[i]
      if(curr[0] == '1'):
         curr = xor(curr , div)
      else :
         curr = xor(curr, z)
      i+=1
   return curr 
def main():
   #Cyclic Redundancy Check
   Input = open('input.txt', 'r')
   Md = Input.read()
   data, div = Md.split('|')
   divLen = len(div)
   data += "0"*(divLen-1)
   print("data before binary division: " , data)
   print()
   CRC = divide(data, div)
   #sender
   data = data[0:-1*(divLen-1)] + CRC
   print("Sender Side:\n{:<13}{:<16}{:<16}\n".format("","Data","CRC"))
   print("{:<13}{:<16}{:<16}".format("",data, CRC))
   print()
   #receiver
   print("Receiver Side:\n")
   print("{:<13}{:<16}{:<16}{:<16}\n".format("","Data","CRC","remainder"))
   Remainder = divide(data,div)
   print("{:<13}{:<16}{:<16}{:<16}\n".format("no error",data, CRC , Remainder))
   changebit = data[len(data)-1]
   if(changebit == "0"):
      data = data[:-1]+"1"
   else :
      data = data[:-1]+"0"
   Remainder = divide(data,div)
   print("{:<13}{:<16}{:<16}{:<16}\n".format("error",data, CRC , Remainder))
   
   
if __name__ == "__main__":
   main()
