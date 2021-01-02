class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print(self.channel, self.volume, self.on)

    # getter, setter
    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel

# 텔레비젼 객체 생성
television = Television(9,10, True)
television.show()

# 채널 변경
television.setChannel(11)
television.show()
