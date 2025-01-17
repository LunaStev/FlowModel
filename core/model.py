import torch.nn as nn

class FlowModel:
    def __init__(self):
        self.model = None

    def build_model(self):
        self.model = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def get_model(self):
        return self.model