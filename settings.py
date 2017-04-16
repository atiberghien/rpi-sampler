from utils import Sample

samples = {
    # touche clavier : sample
    "1" : Sample("Basse", "./bass.wav"),
    "2" : Sample("Cloches", "./bells.wav"),
    "3" : Sample("Clap", "./clap.wav"),
    "4" : Sample("Guitare", "./guitar.wav"),
}

gpio_key_assoc = {
    #pin sur le rasp : touche clavier
    "17" : "1",
    "18" : "2",
    "22" : "3",
    "27" : "4",
}
