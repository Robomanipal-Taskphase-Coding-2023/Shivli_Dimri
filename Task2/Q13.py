class laboratory : 
    def __init__(self):
        
        self.L = [] #initialise the L as an empty list 
        self.n = 0 #initialise n with 0
        self.item_info  = [] #initialise all
        self.quantity = 0
        self.item_name = ''
     


        self.creating_initial_list()
        
        #self.adding_items()


    def creating_initial_list(self): 
        print('create intial list  ')
        self.n = int(input('enter number of initial items in the list : '))
        self.L =[]
        i =0
        while i <self.n : 
            self.item_name = str(input('enter item name : '))
            self.quantity = int(input('enter item quantity : '))
            self.item_info = [self.item_name,self.quantity]    #declaring a list of two parameters. use [] not () thats a tuple 
  #create a list of two parameters (item name and quantity) in each iteration and then we can append this list to the L list. 
            self.L.append(self.item_info)
   
            i+=1
        print(self.L)  
        self.what_you_wanna_do()

    def what_you_wanna_do(self):
        input_n = str(input('ADD_ITEM / DELETE_ITEM '))
        if input_n == 'ADD_ITEM':
            self.adding_items()
        elif input_n == 'DELETE_ITEM' : 
            self.delete_items()
        else : 
            print('invalid input')

    def adding_items(self) :
        to_be_added = str(input('Item to be added_'))
        how_much = int(input('enter how much of it you wanna add : '))
        for self.item_info in self.L:
            if to_be_added == self.item_info[0]:
                self.item_info[1] = self.item_info[1]+ how_much  # Increase the quantity of the existing item
                print('new list is : ',self.L)
                
            else:
              print('Item does not exist.')
        

    def delete_items(self):
        to_be_deleted = str(input('item to be deleted : '))
        how_much_del = int(input('enter how much you wanna delete : '))
        for self.item_info in self.L:
            if to_be_deleted == self.item_info[0]:
                self.item_info[1] = self.item_info[1]- how_much_del  # decrease the quantity of the existing item
            
                
            else:
                print('Item does not exist.')
        print('new list is : ',self.L)

       
    
        


lab = laboratory()  # you need to create an instance objectof the provided classr
