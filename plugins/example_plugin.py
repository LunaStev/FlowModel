class ExamplePlugin:
    def __init__(self):
        print("ExamplePlugin initialized.")

    def modify_model(self, model):
        print("ExamplePlugin: Modifying the model.")
        return f"{model}_modified_by_example"

    def on_train_start(self):
        print("ExamplePlugin: Training started.")

    def on_train_end(self):
        print("ExamplePlugin: Training finished.")
