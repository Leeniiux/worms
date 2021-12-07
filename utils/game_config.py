class Config:

    WINDOW_W = 860
    WINDOW_H = 540
    window = 0

    running = False

    @staticmethod
    def init():
        Config.running = True
