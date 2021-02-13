def main():
   #Hamming Code Error Detection and Correction
   print("Enter data for transmission:", end = " ")
   data = input()
   print("enter 0 for even and 1 for odd parity")
   eo = int(input())
   n = len(data)
   pn = 0
   while(n >= (1<<pn)):
      pn+=1
   
   m = dict() #paritybit - correspoding bits
   for i in range(1,n+pn+1):
      if(i&(i-1)==0 ):
         m[i] = 0
   
   for p,v in m.items():
      d = len(data)-1
      for i in range(1,n+pn+1):
         if(i&(i-1)!=0 and i&p == p ):
            print(i,"{",data[d],"}", end= " ")
            if(data[d]=='1'):
               m[p]+=1
         if(i&(i-1)!=0):
            d-=1 
      print("--->" , p)
      if(m[p]%2 != eo):
         m[p] = 1
      else :
         m[p]= 0
   print(m, pn , n )  
   s = ""
   d= len(data)-1  
   for i in range(1,n+pn+1):
      if(i&(i-1) == 0):
         s = str(m[i]) +s
      else :
         s = data[d] +s
         d-=1
   print("data transmitted : " , s , s == "1010010")
   
   print("Enter Received Data: ")
   data = input()
   #detection
   dl = len(data)
   print("len" , dl)
   for i in range(1,dl+1):
      if(i&(i-1)==0 ):
         m[i] = 0
   for p,v in m.items():
      for i in range(1,dl+1):
         if(i&p == p ):
            if(data[dl-i]=='1'):
               m[p]+=1
      if(m[p]%2 != eo):
         m[p] = 1
      else :
         m[p]= 0
   print(m)
   at = 0 
   for p,v in m.items():
      if v ==1 :
         at +=p
   if(at == 0):
      print("no error detected")
   else :
      print("error detected at:" ,at , 'bit')
      
if __name__ == "__main__":
   main()
