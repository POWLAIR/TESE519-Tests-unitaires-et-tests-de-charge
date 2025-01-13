import os
import shutil
from interfaces import IFileSystem

class FileSystem(IFileSystem):
    def copy_file(self, source: str, destination: str) -> None:
        shutil.copy2(source, destination)
    
    def move_file(self, source: str, destination: str) -> None:
        shutil.move(source, destination)
    
    def delete_file(self, path: str) -> None:
        os.remove(path)
    
    def delete_directory(self, path: str) -> None:
        shutil.rmtree(path) 