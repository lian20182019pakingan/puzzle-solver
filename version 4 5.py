#this function will get the lines
#the target number is number
#the number_set is the list of armies you have
#multiply means number of Multiplication
def get_lines(number,number_set,multiply):
   result=[]
   with open('x.txt') as f:
      for line in f:
         new_line = line.replace("\n", "")
         parse_line=new_line.split("\t")
         if(int(parse_line[2])==number):
            #check that every number of parse_line[1] is in number_set
            list_as_string=parse_line[1]
            list_as_string=list_as_string.replace("[", "")
            list_as_string=list_as_string.replace("]", "")
            list_as_string=list_as_string.replace(" ", "")
            list_of_numbers_as_string=list_as_string.split(",")
            
            Nunber_not_in_set=False
            
            for each_number in list_of_numbers_as_string:
               #check that int(each_number) is in number_set
               if(int(each_number) not in number_set):
                  Nunber_not_in_set=True

            if(not(Nunber_not_in_set)):
               #check if number of Multiplication is less than or equal to multiply
               if(new_line.count('*')<=multiply):
                  result.append(new_line)    
   return result


#this will find all possible sates from the start
def all_states(soldiers_list,monster_list,multiplication_left):
   #this is the index
   i=0
   #this is the result
   result=[[soldiers_list,monster_list,multiplication_left]]
   #this is the list of seen states
   seen_states=[[soldiers_list,monster_list,multiplication_left]]
   #this is the first in first out data structure
   FIFO=[[soldiers_list,monster_list,multiplication_left]]
   while(len(FIFO)>0):
      #remove the fist element of FIFO
      first=FIFO.pop(0)
      #getting all all lines
      the_lines=get_lines(first[1][-1],first[0],first[2])
      for each_line in the_lines:
         parse_line=each_line.split("\t")
         #remove the used numbers from soldiers_list
         list_as_string=parse_line[1]
         list_as_string=list_as_string.replace("[", "")
         list_as_string=list_as_string.replace("]", "")
         list_as_string=list_as_string.replace(" ", "")
         list_of_numbers_as_string=list_as_string.split(",")
         new_list=first[0][:]
         for each_number in list_of_numbers_as_string:
            new_list.remove(int(each_number))
         #remove the last elmement of first[1]
         new_list2=first[1][:]
         new_list2.pop()
         #and decrease first[2] by number of *
         new_number=first[2]-each_line.count('*')
         
         
         
         new_state=[new_list,new_list2,new_number]
         if(new_state not in seen_states):
            seen_states.append(new_state)
            FIFO.append(new_state)
            

            #adding the equation and the index into new state
            new_state.append(i)
            new_state.append(parse_line[0]+"="+str(first[1][-1]))
            result.append(new_state)
            #check if monster_list is empty
            if(new_state[1]==[]):
               return result
      #increase index by 1
      i=i+1
   return result

def solver(soldiers_list,monster_list,multiplication_left):
   result=[]
   #get the list from from_start
   list_of_states=all_states(soldiers_list,monster_list,multiplication_left)
   #getting final game state
   final=list_of_states[-1]
   #adding into the result
   result.append(final[-1])
   index=final[-2]
   
   while(True):
      current_state=list_of_states[index]
      #adding into the result
      result.append(current_state[-1])
      #getting the index
      index=current_state[-2]
      if(index==0):
         return result
      
   
   
every_state=solver([2,3,4,5,6,7,8,9,10,11,12,13,14],[9,16,14,168,72,176],4)
for each_state in every_state:
   print(each_state)

