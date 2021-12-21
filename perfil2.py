import time
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from random import randint
import os
import config


PERFIL = StringSession("1AZWarzoBu5pxuu1UfADsh6fIJhnXJn_rLy47yLKz6RcZpZeBhkwq8Oym4q0-wl2l3KFyRfjhSHQfz6YDxcbYEJ5iBzNEldDc7PmnRsxM13L8uPTV1zYmyJ_U6F0kOeOMdsuCYbTshgl8hSb_sZ_yYJ2IQNruQHqlGxxHWsm2YtKeyoE1VJdrlzFV8KiAPymAZnsrbGlpYRs--6Rf-at33Y8kBvNhlrILKSL_fSSX87P3mytsH0u5Td_kHgtweaS-w5ORT9vdNi99Zcp2D_jdFqjT7Qlm3YMC5FKQghv6esTeHIngMJSXrIGf49M-2pGsTqKkSFSsNR4PMbBnfItwNSIH0W6Ql3s=")

a = 0

Forest , Swamp , Valley , RandomQuest , Foray = False , False , False , False , False

with TelegramClient( PERFIL ,config.API_ID , config.API_HASH ,sequential_updates=True) as client:
	
	@client.on(events.NewMessage(chats=408101137,incoming=True)) #CW bot 
	async def new_quest_handle(event):
	    
	    global  Forest , Swamp , Valley , RandomQuest , a 

	    if "your warehouse is full and you lost your loot" in event.raw_text:
	    	await client.send_message(config.GRUPO_ADM,"Stock Full❗")
		            	    
	    if "You defended villagers well. In exchange for your help," in event.raw_text :
	    	cantidad = event.raw_text[event.raw_text.find("carry ")+6:event.raw_text.find("\n")-2]
	    	time.sleep(randint(8,25))
	    	await client.send_message("chtwrsbot",f"/sc_07_{cantidad}")	    		    		    
 	    
	    if "You were strolling around on your horse when you noticed" in event.raw_text:
	        time.sleep(randint(8,25))
	        await event.click(0)
	             
	
	    if "Stamina restored." in event.raw_text:
	        await client.send_message('chtwrsbot','🗺Quests')
	        Swamp = True
	        a=1
	
	    time.sleep(randint(3,5))	    
	    
	    if a==1:
	        if "Many things can happen in the forest." in event.raw_text:
	            if Forest:
	                time.sleep(3)
	                await event.click(0, 0)
	
	            elif Swamp:
	                time.sleep(3)
	                await event.click(0,1)
	                    
	            elif Valley:
	                time.sleep(3)
	                await event.click(0,2)
	
	            elif RandomQuest:
	                time.sleep(3)
	                await event.click(0,randint(0,2))
	             
	        n = 0	        
	        for i in config.REST :
		        
		        if i in event.raw_text  and "stands victorious over" not in event.raw_text  and "your warehouse is full and you lost your loot" not in event.raw_text and n == 0:
		            
		            if "🧩" in event.raw_text or "📃" in event.raw_text  :
		            	
		            	await client.send_message(config.GRUPO_ADM,event.raw_text)
	            	            
		            time.sleep(randint(5,8))
	            	            
		            await client.send_message('chtwrsbot','🗺Quests')
		            
		            n += 1
		        			            	
		            
		            	            
			        	
	 #arenas
	    if a==2:
	        if "stands victorious over" in event.raw_text or "You didn’t find an opponent. Return later" in event.raw_text:
	            await client.send_message('chtwrsbot','▶️Fast fight')
	
	        if "Not enough gold to pay the entrance fee." in event.raw_text or "It's hard to see your opponent in the dark" in event.raw_text or  "You need to heal your wounds " in event.raw_text or "You should heal up a bit first." in event.raw_text :
	            a=0
	            time.sleep(3)
	            await client.send_message('chtwrsbot','🏅Me')
	            time.sleep(4)
	            await client.send_message("chtwrsbot","🛡Defend")
	            
	              
	
	
	    if "Not enough stamina. " in event.raw_text:
	        a=0
	        time.sleep(4)
	        await client.send_message('chtwrsbot','🛡Defend')
	
	    if "Battle is coming" in event.raw_text:
	        a=0
	        time.sleep(4)
	        await client.send_message('chtwrsbot','🛡Defend')
	        

	           
	@client.on(events.NewMessage(chats=config.GRUPO_ADM)) 
	#Chat de control
	async def new_group_handle(event):
	    
	    global Forest , Swamp , Valley  , RandomQuest , a
	
	    if "/stopQuest" == event.raw_text:
	        Forest = Swamp = Valley = RandomQuest = False
	        a=0
	    
	    if "/RandomQuest" == event.raw_text:
	        RandomQuest = True
	        Forest = Swamp = Valley = False
	        await client.send_message('chtwrsbot','🗺Quests')
	        a=1
	
	    if "/Forest" == event.raw_text:
	        Forest = True
	        Swamp = Valley = RandomQuest = False
	        await client.send_message('chtwrsbot','🗺Quests')
	        a=1
	
	    if "/Swamp" == event.raw_text:
	        Swamp = True
	        Forest = Valley = RandomQuest = False
	        
	        await client.send_message('chtwrsbot','🗺Quests')
	        a=1
	
	    if "/Valley" == event.raw_text:
	        Forest = Swamp = RandomQuest = False
	        Valley = True
	        
	        await client.send_message('chtwrsbot','🗺Quests')
	        a=1
	
	    if "/FastFight" == event.raw_text:
	        a=2
	        await client.send_message('chtwrsbot','▶️Fast fight')
	    if "🦈" == event.raw_text or "🦌" == event.raw_text or "🦅" == event.raw_text or "🐺" == event.raw_text or "🐉" == event.raw_text or "🌑" == event.raw_text or "🥔" == event.raw_text or "🛡" == event.raw_text :	        	        
	        if event.raw_text == "🛡" :
	            await client.send_message('chtwrsbot','🛡Defend')				
	        else :			      	        
	            await client.send_message('chtwrsbot',event.raw_text)
					    	
	print(time.asctime(), '-', '⛓[TDP]Doggy⚒📦⁶⁴')
	
	client.loop.run_forever()
	
	print(time.asctime(), '-', 'Stopped!')
		
