from abc import ABC, abstractmethod
from typing import List

class IFileSystem(ABC):
    @abstractmethod
    def copy_file(self, source: str, destination: str) -> None:
        pass
    
    @abstractmethod
    def move_file(self, source: str, destination: str) -> None:
        pass
    
    @abstractmethod
    def delete_file(self, path: str) -> None:
        pass
    
    @abstractmethod
    def delete_directory(self, path: str) -> None:
        pass

class IFileExplorer(ABC):
    @abstractmethod
    def get_current_path(self) -> str:
        pass
    
    @abstractmethod
    def list_directory(self, path: str) -> List[str]:
        pass
    
    @abstractmethod
    def is_directory(self, path: str) -> bool:
        pass
    
    @abstractmethod
    def navigate_to(self, path: str) -> None:
        pass
    
    @abstractmethod
    def get_parent_directory(self, path: str) -> str:
        pass 