import argparse
import os
import importlib

def check_plugins(loaded_plugins):
    print("Loaded plugins:")
    for plugin in loaded_plugins:
        print(f"- {plugin}")


def train_model(dataset_name, plugins):
    dataset = {'train': []}  # Placeholder for training data

    model = "FlowModel"

    for plugin in plugins:
        if hasattr(plugin, 'modify_model'):
            model = plugin.modify_model(model)

    for plugin in plugins:
        if hasattr(plugin, 'on_train_start'):
            plugin.on_train_start()

    print(f"Training started on dataset: {dataset_name}")

    for plugin in plugins:
        if hasattr(plugin, 'on_train_end'):
            plugin.on_train_end()

    print("Training finished.")


def load_plugins():
    plugins_dir = './plugins'
    plugins = []

    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir)
        print(f"Plugins directory created at {plugins_dir}. Add your plugins there!")

    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            plugin_name = filename[:-3]
            try:
                plugin_module = importlib.import_module(f'plugins.{plugin_name}')
                plugin_class = getattr(plugin_module, plugin_name.title().replace('_', ''), None)
                if plugin_class:
                    plugins.append(plugin_class())
                    print(f"Plugin {plugin_name} loaded.")
                else:
                    print(f"No class found in plugin {plugin_name}.")
            except Exception as e:
                print(f"Failed to load plugin {plugin_name}: {e}")

    return plugins


def predict_model(plugins):
    print("Prediction started.")
    for plugin in plugins:
        if hasattr(plugin, 'on_predict'):
            plugin.on_predict()
    print("Prediction finished.")


def main():
    parser = argparse.ArgumentParser(description="FlowModel CLI")
    parser.add_argument('command', choices=['train', 'predict', 'check_plugins'], help="Command to run")

    args = parser.parse_args()

    plugins, loaded_plugins = load_plugins()

    if args.command == 'train':
        plugins = load_plugins()
        train_model("mnist", plugins)
    elif args.command == 'predict':
        predict_model(plugins)
    elif args.command == 'check_plugins':
        check_plugins(loaded_plugins)


if __name__ == "__main__":
    main()
