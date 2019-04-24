import torch


class Network (object):
    def __init__(self, pretrained_arch, classifier, model):
        self.pretrained_arch = pretrained_arch
        self.classfier = classifier
        self.model = model

    def print_infreezed_layers(self):
        pass

    def unfreeze_all_layers(self):
        pass

    def freeze_pretrained_arch(self):
        pass

    def get_model(self):
        pass

    def load_model_from_checkpoint(self):
        pass

    def save_model_checkpoint(self):
        pass
