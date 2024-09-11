#dataA = {
    #'name' : 'Kuzi',
    #'age' : '103',
    #'birth' : 'Gitsukh',}
#dataB = {
    #'name' : "Buk'tu",
    #'age' : '23',
    #'birth' : 'Rikaya',}

Datas = {
    'dataA' : {
     'name' : 'Kuzi',
     'age' : '103',
     'birth' : 'Gitsukh',
    },
    
    'dataB' : {
     'name' : 'Buktu',
     'age' : '23',
     'birth' : 'Rikaya',
    },
}

num = 0
null = ''
coreActive = True

prompt = "\nWelcome to Ishgrayuz Data Center (I.D.C.)"
prompt +="\n-----------------------------------------"
print (prompt)

while coreActive :
    
    print(" new - input new data\n print - display data\n exit - to terminate")
    key = input()

    if key == 'new' :
        datName = 'data' + str(num)
        datLocal = {}
        datLocal['name'] = input("\n Input name :")
        datLocal['age'] = input("\n Input age :")
        datLocal['birth'] = input("\n Input birth place :")
        Datas[datName] = datLocal
        num += 1
        print ('\nData has been input successfuly!')
        print ("-----------------------------------------")

    if key == 'print' :
        print('\n What to print? :\n - list\n - person\n type "return" to go back')
        print ("-----------------------------------------")
        while True :

            S_key = input()

            if S_key == 'list' :
                
                if len(Datas.items()) == 0:
                    print ("\n List does not contain any data!")
                    print ("-----------------------------------------")
                    continue
                
                else :
                    for data, local in Datas.items() :
                        print (f"\nDirectory : {data}")
                        for info, spec in local.items() :
                            print (f"{info} : {spec}")
                    print ("-----------------------------------------")

            elif S_key == 'person' :
                
                if len(Datas.items()) == 0:
                    print ("\n No database in the directory!")
                    print ("-----------------------------------------")
                    continue
                
                else :

                    
                    for data, local in Datas.items() :
                        #name = local.get('name')
                        print (f"{data} : {local.get('name')}")
                        
                    print ('\nWhich data would you like to access?')
                    print ("-----------------------------------------")

                    keyData = input()
                    if keyData in Datas.keys() :
                        for info, spec in Datas.get(keyData).items() :
                            print (f"{info} : {spec}")
                        print ("-----------------------------------------")

            elif S_key == "return":
                break
            
            else :
                print ("Invalid KEY")
                print ("-----------------------------------------")
                continue
            

    if key == 'exit' :
        print ('Goodbye!')
        print ("-----------------------------------------")
        break

