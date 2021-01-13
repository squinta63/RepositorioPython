import random

def random_walk(n):
    # Return coordinates after 'n' block random walk.
    x, y = 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(1, 0), (0, 1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    
    return(x, y)

#for i in range(25):
    #walk = random_walk(10)
    #print(walk, 'Distance from home =', abs(walk[0]) + abs(walk[1]))

# What is teh longes random walk you can take so that on average you will end up 
# 4 bloks or fewer from home?. There is less than a 50% you will pay for transport home.

number_of_walks = 40000

for walk_length in range(1, 31):
    no_transport = 0 # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    
    no_transport_percentage = float(no_transport / number_of_walks)

    print("Walk size =", walk_length, "/ % of no transport", round(100*no_transport_percentage, 2))
