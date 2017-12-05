import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import random 
import tkinter
import requests
import bs4



# Initalising the model using x and y data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)



# Calculate the distance between the agents using pythagoras
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5



# Creating the environment for the agents to move around in 
# Creating the agent list
environment = []
agents = []



# Defining the area for animation
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])



# Stating how many agents and iterations will be in the ABM
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20



# Read the csv, and add the data
f=open('in.txt', newline='')
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
f.close() 



# Make the agents, using the agent class
# Passing the environment list into the constructor of the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))
    
    

# Creating the animation function
carry_on = True
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
    

def update (frame_number): 
    fig.clear()
    global carry_on

                
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        matplotlib.pyplot.imshow(environment)
        #print(agents[i][0],agents[i][1])


def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a		
        a = a + 1



# Displaying the animation within the environment
# Meaning that the agents move around within the environment
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()



# Making a Graphical User Interface that displays the model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()


# Build the main window, so that the environment is displayed 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkagg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)    
    
    
    
# Allow the user interface to wait for events that are inputted
tkinter.mainloop()







"""


# Calculating the distance between the agents        
for j in range(num_of_agents):
   for i in range(num_of_agents):
        distance = distance_between(agents[i].x, agents[i].y)
print(distance)

    if random.random() < 0.5:#           
        agents[i][0] = (agents[i][0] + 1) % 100
    else:
        agents[i][0] = (agents[i][0] - 1) % 100

    if random.random() < 0.5:
           agents[i][1] = (agents[i][1] + 1) % 100
    else:
           agents[i][1] = (agents[i][1] - 1) % 100



# Make a single agent
a = agentframework.Agent()
print (a.y, a.x)
a.move()
print (a.y, a.x)

"""

