class Missile:
    x=0
    y=0
    def __init__(self, planeX, planeY):
        self.x=planeX
        self.y=planeY

    def destruction(self):
        while(self.y<-1080):
            self.y-=5

