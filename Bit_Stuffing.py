def main():
   #BitStuffing
   #open and read the data from the file
   Input = open("input.txt" , "r")
   data = Input.read()
   print("data brfore stuffing :" , data)
   c = 0
   s= ""
   for each in data :
      s += each 
      if(each == '1'):
         c+=1
      else :
         c= 0
      if(c == 5):
         s+='0'
         c= 0
   print("data after stuffing:" , s )
   #writing stuffed data back to output file
   Output = open ('output.txt' , 'w')
   Output.write(s)
   Output.close()
if __name__ == "__main__":
   main()
