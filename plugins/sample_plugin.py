class SamplePlugin:
    def __init__(self):
        print("SamplePlugin initialized.")

    def modify_model(self, model):
        print("SamplePlugin: Modifying the model.")
        return model

    def on_train_start(self):
        print("SamplePlugin: Training started.")

    def on_train_end(self):
        print("SamplePlugin: Training finished.")
