from enum import Enum

from modules.console import console
from modules.context import context
from modules.memory import get_task, read_symbol, get_event_flag, get_game_state, GameState
from modules.pokemon import get_party

class ModeWynautEggStates(Enum):
    RESET = 0
    OVERWORLD = 1
    TITLE = 2


class WynautEgg:
    def __init__(self) -> None:
        self.state: ModeWynautEggStates = ModeWynautEggStates.RESET
        self.party_count = read_symbol("gPlayerPartyCount", size=1)[0]

        context.emulator.press_button("A")
                        
        #save game
        #Must be Emerald Game
        #Must be in position x, facing lady
        #Must save game before recieving egg??
        #Must have 1 inventory space
            #if pokemon.is_shiny == True:
            #    console.log(pokemon.name)
            #else:
            #    console.log(pokemon.name)

    def update_state(self, state: ModeWynautEggStates):
        self.state: ModeWynautEggStates = state

    def step(self):
        #party_count = read_symbol("gPlayerPartyCount", size=1)[0]

        #if(party_count <= 5): #IF inventory not full interact with lady
            
        #FLAG_RECEIVED_LAVARIDGE_EGG    
            while True: 
                match self.state:
                    case ModeWynautEggStates.RESET:
                        if not get_event_flag("FLAG_RECEIVED_LAVARIDGE_EGG"):
                            if get_task("TASK_DRAWFIELDMESSAGEBOX2") == {}: # While having messages from the lady.
                                context.emulator.press_button("A")
                            else: # First button press. Didn't start talking with lady yet.
                                context.emulator.press_button("A")# TODO: remove second else, always A
                        else:
                            console.log("finito") #TODO: refactor
                            for pokemon in get_party():
                                if pokemon.location_met == "Traded" and pokemon.name == "EGG":
                                    console.log(pokemon.species.name)
                                    #validate if is shiny
                                    if pokemon.is_shiny == True: 
                                        context.bot_mode = "Manual"
                                        console.log("Fds")
                                    else:
                                        console.log("not shiny")
                                        #context.emulator.re
                                        # 
                                        # set()
                    
                    case ModeWynautEggStates.TITLE:
                            match get_game_state():
                                case GameState.TITLE_SCREEN:
                                    context.emulator.press_button("A")
                                case GameState.MAIN_MENU:  # TODO assumes trainer is in Oak's lab, facing a ball
                                    if get_task("TASK_HANDLEMENUINPUT").get("isActive", False):
                                        context.message = "Waiting for a unique frame before continuing..."
                                        self.update_state(ModeStarterStates.RNG_CHECK)
                                        continue

                                             
                yield
        