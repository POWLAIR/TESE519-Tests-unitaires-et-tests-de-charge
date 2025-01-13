import os
from interfaces import IFileExplorer
from typing import List

class FileExplorer(IFileExplorer):
    def __init__(self):
        self._current_path = os.path.expanduser('~')
    
    def get_current_path(self) -> str:
        return self._current_path
    
    def list_directory(self, path: str) -> List[str]:
        return os.listdir(path)
    
    def is_directory(self, path: str) -> bool:
        return os.path.isdir(path)
    
    def navigate_to(self, path: str) -> None:
        if os.path.isdir(path):
            self._current_path = path
        else:
            raise ValueError(f"Cannot navigate to {path}: not a directory")
    
    def get_parent_directory(self, path: str) -> str:
        return os.path.dirname(path) 