from enum import Enum 

class controls(Enum):
    UP = 1 
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class snake:
    length = None
    controls = None
    body = None
    block_size = None 
    colour = (204, 51, 0)
    bounds = None 

def __init__(self, block_size, bounds):
    self.block_size = block_size
    self.bounds = bounds
    self.respawn()

def respawn(self):
    self.length = 3
    self.body = [(20,20),(20,40),(20,60)]
    self.controls = controls.DOWN

def draw(self, game, window):
    for segment in self.body:
        game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))

def move(self):
    curr_head = self.body[-1]
    if self.direction == controls.DOWN:
        next_head = (curr_head[0], curr_head[1] + self.block_size)
        self.body.append(next_head)
    elif self.direction == controls.UP:
        next_head = (curr_head[0], curr_head[1] - self.block_size)
        self.body.append(next_head)
    elif self.direction == controls.RIGHT:
        next_head = (curr_head[0] + self.block_size, curr_head[1])
        self.body.append(next_head)
    elif self.direction == controls.LEFT:
        next_head = (curr_head[0] - self.block_size, curr_head[1])
        self.body.append(next_head)
    if self.length < len(self.body):
        self.body.pop(0)
