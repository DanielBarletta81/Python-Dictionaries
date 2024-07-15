#Problem Statement: Develop a program that:

#Tracks customer service tickets, each with a unique ID, customer name, issue description,
#  and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.

 #Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:
import random


service_tickets =    { "uniqueId": [117] , "client_name" : ["Daniel"], "issue": ["frozen screen"], "status": ["open"]


 }

new_ticket = {
}


#Open a new service ticket.

def add_ticket(): 

    service_tickets["uniqueId"] = (random.randint(1, 100000)) 
    new_ticket["client_name"] = input("What is the client's name? ")
    new_ticket["issue"] = input("What issue are they having? ") 
    new_ticket["status"] = input("What's the status of this issue(open/closed)? ")   
 
    service_tickets.update(new_ticket)
    
   



#Update the status of an existing ticket.

def status_update():
    try:
       id_match =  int(input("What is the unique id?"))
       if id_match == service_tickets.get("uniqueId"):
        if service_tickets["status"] == "open":
              service_tickets["status"] = "closed"
       else:
            print("That client Id doesn't match.")
            print(service_tickets)  
    except KeyError or ValueError:
        print(KeyError, ValueError)




#Display all tickets or filter by status.

def display_tickets():
    
 
    for value in service_tickets["uniqueId"]:
        value = service_tickets.get("uniqueId")
        print(f'Client Id : {value}')
        for client in service_tickets["client_name"]:
            print(f'Name: {client}')
        for issue in service_tickets["issue"]:
            print(f'issue {issue}')
        for status in service_tickets["status"]:
            print(f'Status: {status}', end ="\n")

    

    
def filter_status():
    for x in service_tickets:
        client_id = int(input("What is the client's unique id? "))
        if client_id in service_tickets["uniqueId"] and service_tickets["status"] == 'open':
            to_update = input("Is this matter considered closed(Yes/No)?")
            if to_update == 'Yes':
                service_tickets["status"] = 'closed'
                break
            else:
                service_tickets["status"] = 'open'
               
            print(f'Ticket Status: {service_tickets["status"]}')
        else:
            print("Unable to find client, please try again.")
    


    



def main_service():
    try:
        while True:
                print(" **** Welcome to your Service Desk Application ****")
                print(" Menu: ")
                print(" 1. Add a client ticket.")
                print(" 2. View open tickets.")
                print(" 3. View all tickets.")
                print(" 4. Update a ticket")
                print(" 5. Quit")


                selection = int(input("Please make a selection (1-5). "))

                if selection == 1:
                    add_ticket()
                elif selection == 2:
                   status_update()
                elif selection == 3:
                    display_tickets()
                elif selection == 4:
                    filter_status()
                else:
                      print("Thank you for your dedication to our clients! Have a nice day.")
                      break
    except ValueError:
        print(ValueError , "Please enter a valid selection, numbers only.")
        if ValueError:
             main_service()  
            

main_service()