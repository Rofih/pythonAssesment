list='''
Welcome to your Nokia phone
1->Phone book
2->Messages
3->Chat
4->Call register
5->Tones
6->Settings
7->Call divert
8->Games
9->Calculator
10->Reminders
11->Clock
12->Profiles
13->SIM services
'''
print(list)

print("Phone book")

main_menu=int(input("Enter a option:"))
match main_menu:	
	case 1:


		book=int(input("Enter a option:"))
		match book:
			case 1:
				print("Search")
			case 2:
				print("Service Nos.")
			case 3:
				print("Add name")
       			case 4:
                		print("Erase")
                        case 5:
                		print("Edit")
			case 6:
                		print("Assign tone")
			case 7:
                		print("Send b'card")
			case 8:
                		
                            view=int(input("Enter a option:"))
                            match view:
 				case 1:
                		       print("Type of view")
				case 4:
                		       print("Memory status")
				

			case 9:
                		print("Speed dials")
                        case 10:
                		print("Voice tags")



	case 2:
		print("Messages")
                        message=int(input("Enter a option:"))
			match message: 
         			case  1:
                			print("Write messages")
               
          			case 2:
                			print("Inbox")
               
          			case 3:
                			print("Outbox")
            
          			case 4:
               				print("Picture messages")
              
          			case 5:
                			print("Templates")
               
          			case 6:
                			print("Smileys")
          
          			case 7:
                			print("Messages settings")
                               		messagesettings=int(input("Enter a option:"))
                			match messagessettings: 
                        			case 1:
                            				print("Set 1")
                                        			set1=int(input("Enter a option:"))
                            					match (set1)
                               						case 1:
                                     						print("Message centre number")
                                   
                               						case 2:
                                     						print("Messages sent as")
                               
                               						case 3:
                                     						print("Message validity")
                              


	
         
                      				case 2: 
                            				print("Common")
                                        		common=int(input("Enter a option:"))
                            				match common: 
                                  				case 1:
                                      					print("Delivery reports") 
                                  				case 2:
                                        				print("Reply via same centre")
                                  
                                  				case 3:
                                        				print("Character support")
                                 
                                  

        		case 8:
             			 print("Info service")
         
        		case 9:
             			 print("Voice mailbox number")
        
        		case 10:
              			 print("Service command editor")
        


	case 3:
      		print("Chat")
	case 4:
      		print("Call register")
                        callregister=int(input("Enter a option:"))
      			match callregister: 
            			case 1:
                  			print("Missed calls")
             
            			case 2:
                  			print("Received calls")
            
            			case 3:
                  			print("Dialled numbers")
            
            			case 4:
                 		 	print("Erase recent call lists")
            
				case 5: 
                 			print("Show call duration")
                                                showcallduration=int(input("Enter a option:"))
                 				match showcallduration: 
                        				case 1:
                              					print("Last call duration")
                        
                        				case 2:
                              					print("All call's duration")
                        
                        				case 3:
                              					print("Received call's duration")
                        
                        				case 4:
                              					print("Dialled call's duration")
                        
                        				case 5:
                              					print("Clear times")
                        

       
				case 6:
 					print("Show call costs")
                                                 showcallcost=int(input("Enter a option:"))
                 				 match showcallcost: 
                        				case 1:
                              					print("Last call cost")
                        
                        				case 2:
                              					print("All call's cost")
                        
                        				case 3:
                              					print("Clear counters")
                        

				case 7:
 					print("Call cost settings")
                                                callcoststtings=int(input("Enter a option:"))
                  				match callcostsettings: 
                        				case 1:
                              					print("Call cost limit")
                         
                        				case 2:
                              					print("Show costs in")
                        

                      
				case 8:
                			print("Prepaid credit")
                                          



	case 5:
      		print("Tones")
                tones=int(input("Enter a option:"))
      		match tones: 
            		case 1:
                  		print("Ringing tone")
              
            		case 2:
                  		print("Ringing volume")
             
            		case 3:
                  		print("Incoming call alert")
             
            		case 4:
                  		print("Composer")
             
            		case 5:
                  		print("Message alert tone")
             
            		case 6:
                  		print("Keypad tones")
             
            		case 7:
                  		print("Warning and game tones")
             
            		case 8:
                  		print("Vibrating alert")
             
            		case 9:
                  		print("Screen saver")
             



	case 6:
      		print("Settings")
                        settings=int(input("Enter a option:"))
      			match settings: 
            			case 1:
                  			print("Callsettings")
                                                callsettings=int(input("Enter a option:"))    
                  				match callsettings: 
                         				case 1:
                               					print("Automatic redial")
                          
                         				case 2:
                               					print("Speed dialling")
                          
                         				case 3:
                               					print("Call waiting options")
                          
                         				case 4:
                               					print("Own number sending")
                          
                         				case 5:
                               					print("Phone line in use")
                          
                         				case 6:
                               					print("Automatic answer")
                          

  
            			case 2:
                  			print("Phone settings")
                                                phonesttings=int(input("Enter a option:"))
                  				match phonesettings: 
                         				case 1:
                               					print("Language")
                          
                         				case 2:
                               					print("Cell info display")
                          
                         				case 3:
                               					print("Welcome note")
                          
                         				case 4:
                               					print("Network selection")
                          
                         				case 5:
                               					print("Lights")
                          
                         				case 6:
                               					print("Confirm SIM service actions")
                          


            			case 3:
                  			print("Security settings")
                                                securitysettings=int(input("Enter a option:"))
                  				match securitysettings: 
                         				case 1:
                               					print("PIN code request")
                          
                         				case 2:
                               					print("Call barring service")
                          
                         				case 3:
                               					print("Fixed dialling")
                          
                         				case 4:
                               					print("Closed user group")
                          
                         				case 5:
                               					print("Phone security")
                          
                         				case 6:
                               					print("Change access codes")
                          


            			case 4:
                  			print("Restore factory settings")
                   



	case 7:
      		print("Call divert")

	case 8:
      		print("Games")

	case 9:
      		print("Calculator")

	case 10:
       		print("Reminders")

	case 11:
       		print("Clock")
                        clock=int(input("Enter a option:"))
       			match clock: 
                         	case 1:
                               		print("Alarm clock")
                          
                         	case 2:
                               		print("Clock settings")
                          
                         	case 3:
                               		print("Date setting")
                          
                         	case 4:
                               		print("Stopwatch")
                          
                         	case 5:
                               		print("Countdown timer")
                         
                         	case 6:
                               		print("Auto update of date and time")
                          



	case 12:
       		print("Profiles")

	case 13:
       		print("SIM services")
          









































