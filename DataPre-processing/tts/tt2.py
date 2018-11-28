from tempfile import TemporaryFile
from gtts import gTTS
import os


# def text_to_speech_gtts(res_ans):
#     volume = 1.0
#     music_file = "ans01.mp3"
#     tts = gTTS(text=res_ans, lang='zh-tw')
#     # os.system("mpg321 good.mp3")
#     tts.save(music_file)


# text_to_speech_gtts('床前明月明月明月明月明月明月87光11')


def text_to_speech_gtts(res_ans):
    volume = 1.0
    tts = gTTS(text=res_ans, lang='zh-tw')
    print(type(tts))
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.close()


text_to_speech_gtts('安安')
