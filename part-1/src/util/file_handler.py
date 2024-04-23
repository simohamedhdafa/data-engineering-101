import os
from datetime import datetime
from util.config_handler import ConfigHandler

class FileHandler(self):
    def __inti__(self):
        self.config_handler = ConfigHandler()
        self.directory = self.config_handler.get_input_dir()
        self.registry_file = self.config_handler.get_registry_file()

    def track_new_files(self):
        all_files = self.list_files()
        processed_files = self.load_registry()
        new_files = [f for f in all_files if f not in processed_files]
        self.update_registry(new_files)
        print(f"[INFO]: listing new files. {new_files}")
        return new_files
    
    def list_files(self):
        files = [f for f in os.listdir(self.directory) if f.endswith(".csv") and os.path.isfile(os.path.join(self.directory, f))]

    def load_registry(self):
        if not os.path.exists(self.registry_file):
            with open(self.registry_file, "r") as f:
                pass 
            return set()
        else: 
            with open(self.registry_file, "r") as f:
                return set(line.split("\t")[0] for line in f.read().splitlines())
            
    def update_registry(self, new_files):
        with open(self.registry_file, "a") as f:
            for filename in new_files:
                f.write(filename + "\t" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")