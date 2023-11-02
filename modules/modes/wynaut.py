from enum import Enum

from modules.console import console
from modules.context import context
from modules.memory import get_task, read_symbol

class ModeWynautEggStates(Enum):
    RESET = 0
    MSG1 = 1
    MSG2 = 2
    MSG3 = 3
    MSG4 = 4
    MSG5 = 5
    MSG6 = 6
    QUESTION = 7
    THANKS_MSG = 8
    CONFIRMATION_MSG = 9
#gStringVar4
#Good! I hope you’ll walk plenty with this here EGG!
class WynautEgg:
    def __init__(self) -> None:
        self.state: ModeWynautEggStates = ModeWynautEggStates.RESET
        self.party_count = read_symbol("gPlayerPartyCount", size=1)[0]
        #Must be Emerald Game
        #Must be in position x, facing lady
        #Must save game before recieving egg??
        #Must have 1 inventory space

    def update_state(self, state: ModeWynautEggStates):
        self.state: ModeWynautEggStates = state

    def step(self):
        #party_count = read_symbol("gPlayerPartyCount", size=1)[0]

        #if(party_count <= 5): #IF inventory not full interact with lady
            
        #FLAG_RECEIVED_LAVARIDGE_EGG    
            while True: 
                match self.state:
                    case ModeWynautEggStates.RESET:
                        context.emulator.press_button("A")
                        #get_emulator().run_single_frame()
                        actual_party_count = read_symbol("gPlayerPartyCount", size=1)[0]
                        if not (actual_party_count == self.party_count+1):
                            if get_task("TASK_DRAWFIELDMESSAGEBOX2") == {}: #First time 
                                context.emulator.press_button("A") # presses 1 time A to chat with lady
                                console.log("a")
                                #get_emulator().run_single_frame()
                            else: #Didn't start talking with lady 
                                context.emulator.press_button("A")
                                #get_emulator().run_single_frame()
                                console.log("else")
                        else:
                            console.log("finito")
                            context.emulator.press_button("A")
                            #get_emulator().run_single_frame()
                            context.bot_mode = "Manual"
                yield

        
#
        