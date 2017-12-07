"""
Author = Georgina Weaver

Core Programming for GIS - Andy Evans, University of Leeds

Defining the agent class to be used within the main model
Developing the behaviour of an agent so it moves and eats within the environment

"""



# Import random to be able to create agents
import random



# Including the environment and agents within this class

class Agent():
    def __init__(self, environment, agents, neighbourhood):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents 
        #self.share_with_neighbours = share_with_neighbours
        self.neighbourhood = neighbourhood
        self.store = 0
        
# Now have x and y coordinates in agent, initialised to random location
# Clearly structured to see what the components are wihtin the agent class



# Moving an agent at random when the model is run 

    def move(self):
        if random.random() < 0.5:
            self.y = (self.y +1) % len(self.environment)
        else:
            self.y = (self.y -1) % len(self.environment)
        
        if random.random() < 0.5:
            self.x = (self.x +1) % len(self.environment)
        else:
            self.x = (self.x -1) % len(self.environment)
            
            
            
# Telling the agents what to eat within the environment

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
      
        
        
# Work out the distance to each of the agents
# If they fall within neighbourhood distance, set it ands its neighbours equal to average

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
            #print("sharing" + str(dist) + " " + str(ave))
            


# Pythagoras distance between the two agents  
         
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
