# by Kami Bigdely
# Extract superclass.
class Shape:
    def __init__(self, x, y, visible = True):
        self.x = x
        self.y = y
        self.visible = visible

    def set_visibility(self):
        if self.visible:
            self.visible = False
        else:
            self.visible = True

class Circle(Shape):
    
    def __init__(self, x, y, r, visible = True):
        super().__init__(x,y,visible)
        self.r = r
      
    def display(self):
        print('drew the circle.')
        
    def get_center(self):
        return self.x, self.y
    
    
class Rectangle(Shape):
    
    def __init__(self, x, y, width, height, visible = True):
        # left-bottom corner.
        super().__init__(x,y,visible)
        # self.x = x
        # self.y = y
        self.width = width
        self.height = height
        # self.visible = visible
        
    def display(self):
        if self.visible:
            print('drew the rectable.')
            
    def hide(self):
        self.visible = False
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visibility()
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.set_visibility()
    rect.display()
    print('center point',rect.get_center())