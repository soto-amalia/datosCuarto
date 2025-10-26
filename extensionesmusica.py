class Audio:
    def __init__(self, nombre):
        if not nombre.endswith(self.ext):
            raise Exception("Formato invalido")
        self.nombre=nombre

""
class MP3(Audio): 
    ext="mp3"
    def play(self):
        print(f"Reproduciendo {self.nombre} como mp3")
class WAV(Audio):
    ext="wav"
    def play(self):
        print(f"Reproduciendo {self.nombre} como un wav")
villancico_mp3=MP3("audio.mp3")
villancico_mp3.play()

cancionWavNavidad=WAV("peces_rio.wav")
cancionWavNavidad.play()