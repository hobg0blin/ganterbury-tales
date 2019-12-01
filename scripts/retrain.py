import gpt_2_simple as gpt2
import os
import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", '--model_name', default='355M')
parser.add_argument("-f", '--file_name')
parser.add_argument("-s", '--steps', default=1000)
args = parser.parse_args()

model_name = args.model_name
print("model name:" + model_name)
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    # model is saved into current directory under /models/124M/
    gpt2.download_gpt2(model_name=model_name)


file_name = args.file_name
if not os.path.isfile(file_name):
    url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    data = requests.get(url)

    with open(file_name, 'w') as f:
        f.write(data.text)


sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=args.steps)   # steps is max number of training steps

gpt2.generate(sess)
