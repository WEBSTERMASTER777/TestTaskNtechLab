import sys
import os
import re
import torch

from facenet_pytorch import InceptionResnetV1
from torchvision import transforms
from PIL import Image
from json import dump
from glob import glob
from yaml import load
from yaml import FullLoader


def load_config(config_file):
    with open(config_file) as f:
        return load(f, Loader=FullLoader)


def load_class_names(filename):
    with open(filename) as f:
        return f.read().splitlines()


def load_image(infilename):
    transform = transforms.Compose([
        transforms.RandomResizedCrop((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    img = Image.open(infilename)
    img = transform(img)
    img = img.reshape(1, 3, 256, 256)
    return img


def write_json_file(filename, data, indent=2):
    with open(filename, "w") as write_file:
        dump(data, write_file, indent=indent)


def get_predict(img, classifier, classes_names):

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = InceptionResnetV1(num_classes=2, classify=True)
    model.load_state_dict(
        torch.load(
            classifier,
            map_location=device))
    model.eval()
    inputs = load_image(img)
    pred_list = model(inputs).sort(descending=True)[1].tolist()
    classes_label = load_class_names(classes_names)

    return classes_label[pred_list[0][0]]


def create_json(path, classifier, class_name, save_path):
    items = {}
    for img in os.listdir(path):

        if re.search(r"jpg|jpeg", img):

            pred = get_predict(os.path.join(path, img), classifier, class_name)

            items[img] = pred

    with open(save_path, 'w') as f:
        dump(items, f)


if __name__ == '__main__':

    config = load_config('script_config.yaml')
    path = sys.argv[1]

    create_json(
        path,
        config['classifier'],
        config['classes_names'],
        config['save_json'])
