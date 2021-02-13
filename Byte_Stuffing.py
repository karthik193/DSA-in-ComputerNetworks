def main():
   #ByteStuffing
   Input = open('input.txt', 'r')
   data = Input.read()
   Input.close()
   print("data before stuffing:", data)
   n = len(data)
   s= ""
   i = 0 
   while(i<n):
         if(i+3 <= n):
                if(data[i:i+3] == 'DLE' or data[i:i+3] == 'ESC'):
                   s += 'ESC'
                   s+= data[i:i+3]
                   i+=3
                   continue 
      
         s += data[i]
         i+=1
   s = "DLE STX" +s + "DLE ETX"
   print("data after stuffing:" ,s)
   #print(s , s == "DLE STXABESCDLEGHESCESCKLDLE ETX")
   Output = open('output.txt', 'w')
   Output.write(s)
   Output.close() 
                   
if __name__ == "__main__":
   main()
