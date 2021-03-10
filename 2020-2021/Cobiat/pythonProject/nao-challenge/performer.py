import thread
from naoqi import ALProxy


class Performer:
    def __init__(self, nao_ip, nao_port, init_pos):
        self.nao_ip = nao_ip
        self.nao_port = nao_port
        init_pos.main(self.nao_ip, self.nao_port)

    def play_music(self, path, foo):
        aup = ALProxy("ALAudioPlayer", self.nao_ip, self.nao_port)
        aup.playFile(path)

    def perform(self, list_of_pos, music_path):
        thread.start_new_thread(self.play_music, (music_path, ''))

        for position in list_of_pos:
            position.main(self.nao_ip, self.nao_port)
