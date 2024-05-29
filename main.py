import ChatTTS
from IPython.display import Audio

chat = ChatTTS.Chat()
chat.load_models(source = "local", local_path='/home/u210110703/.cache/modelscope/hub/pzc163/chatTTS')

texts = ["我觉得像我们这些写程序的人，他，我觉得多多少少可能会对开源有一种情怀在吧我觉得开源是一个很好的形式。现在其实最先进的技术掌握在一些公司的手里的话，就他们并不会轻易的开放给所有的人用。",]

wavs = chat.infer(texts, use_decoder=True)
Audio(wavs[0], rate=24_000, autoplay=True)