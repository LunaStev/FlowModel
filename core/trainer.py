import torch.optim as optim
import torch.nn as nn

class Trainer:
    def __init__(self, model):
        self.model = model
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.01)

    def train(self, train_loader, epochs=5):
        for epoch in range(epochs):
            for images, labels in train_loader:
                self.optimizer.zero_grad()
                outputs = self.model(images.view(-1, 28*28))
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()

            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")