#SDK模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('pzc163/chatTTS')

print(model_dir)