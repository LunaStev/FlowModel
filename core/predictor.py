import torch

class Predictor:
    def __init__(self, model):
        self.model = model

    def predict(self, test_loader):
        self.model.eval()
        predictions = []

        with torch.no_grad():
            for images, _ in test_loader:
                outputs = self.model(images.view(-1, 28 * 28))
                _, predicted = torch.max(outputs, 1)
                predictions.extend(predicted.cpu().numpy())

        return predictions
