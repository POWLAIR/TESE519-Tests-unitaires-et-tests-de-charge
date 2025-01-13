import os
import shutil
from typing import List
from interfaces import IFileSystem, IFileExplorer

""" File Manager Console Application 
    Generated with Claude 3.5 Haiku
    With 2 prompts : 
        Génère un programme console python qui permet d'explorer les fichiers, 
        en sélectionner pour copier, déplacer et supprimer les fichiers sélectionnés. 
        Une classe "métier" regroupe les fonctions de sélection, copie, déplacement 
        et suppression.

        Deux rectifications : il faudrait passer le code et l'interface en anglais 
        et sortir la sélection de la classe "métier"
"""


class FileSelector:
    def __init__(self):
        self.selected_files = []
        self.current_directory_contents = []

    def load_directory_contents(self, directory_path):
        """Load the contents of a directory"""
        try:
            self.current_directory_contents = os.listdir(directory_path)
            return self.current_directory_contents
        except Exception as e:
            print(f"Error loading directory contents: {e}")
            return []

    def select_files_by_indices(self, indices, directory_path):
        """Select files based on indices"""
        try:
            # Convert input string to list of indices
            selected_indices = [int(i.strip()) for i in indices.split(',')]
            
            # Reset previous selection
            self.selected_files.clear()
            
            # Select files
            for index in selected_indices:
                if 0 <= index < len(self.current_directory_contents):
                    full_path = os.path.join(directory_path, self.current_directory_contents[index])
                    self.selected_files.append(full_path)
            
            print("Selected files:")
            for file in self.selected_files:
                print(f" - {os.path.basename(file)}")
            
            return self.selected_files
        except ValueError:
            print("Invalid input. Please enter valid indices.")
            return []
        except Exception as e:
            print(f"Error selecting files: {e}")
            return []

    def get_selected_files(self):
        """Return the list of currently selected files"""
        return self.selected_files

    def clear_selection(self):
        """Clear the current file selection"""
        self.selected_files.clear()


class FileManager:
    def __init__(self, file_system: IFileSystem, file_explorer: IFileExplorer, file_selector: 'FileSelector'):
        self._file_system = file_system
        self._file_explorer = file_explorer
        self._file_selector = file_selector

    def display_directory_contents(self) -> List[str]:
        """Display contents of the current directory"""
        try:
            current_path = self._file_explorer.get_current_path()
            contents = self._file_explorer.list_directory(current_path)
            return contents
        except Exception as e:
            raise RuntimeError(f"Error displaying directory contents: {e}")

    def navigate(self, index: int) -> None:
        """Navigate to a subdirectory"""
        try:
            current_path = self._file_explorer.get_current_path()
            contents = self._file_explorer.list_directory(current_path)
            selected_path = os.path.join(current_path, contents[index])
            
            if self._file_explorer.is_directory(selected_path):
                self._file_explorer.navigate_to(selected_path)
            else:
                raise ValueError(f"Cannot navigate to {selected_path}: not a directory")
        except Exception as e:
            raise RuntimeError(f"Navigation error: {e}")

    def go_to_parent_directory(self) -> None:
        """Move to the parent directory"""
        current_path = self._file_explorer.get_current_path()
        parent_path = self._file_explorer.get_parent_directory(current_path)
        self._file_explorer.navigate_to(parent_path)

    def copy_files(self, destination: str) -> None:
        """Copy selected files"""
        try:
            for file in self._file_selector.get_selected_files():
                self._file_system.copy_file(file, destination)
            self._file_selector.clear_selection()
        except Exception as e:
            raise RuntimeError(f"Copy error: {e}")

    def move_files(self, destination: str) -> None:
        """Move selected files"""
        try:
            for file in self._file_selector.get_selected_files():
                self._file_system.move_file(file, destination)
            self._file_selector.clear_selection()
        except Exception as e:
            raise RuntimeError(f"Move error: {e}")

    def delete_files(self) -> None:
        """Delete selected files"""
        try:
            for file in self._file_selector.get_selected_files():
                if self._file_explorer.is_directory(file):
                    self._file_system.delete_directory(file)
                else:
                    self._file_system.delete_file(file)
            self._file_selector.clear_selection()
        except Exception as e:
            raise RuntimeError(f"Delete error: {e}")


def main_menu():
    file_manager = FileManager()
    
    while True:
        print("\n--- File Explorer ---")
        print("1. Display Directory")
        print("2. Navigate")
        print("3. Go to Parent Directory")
        print("4. Select Files")
        print("5. Copy")
        print("6. Move")
        print("7. Delete")
        print("8. Quit")
        
        choice = input("Your choice: ")
        
        try:
            if choice == '1':
                file_manager.display_directory_contents()
            
            elif choice == '2':
                index = int(input("Enter navigation index: "))
                file_manager.navigate(index)
            
            elif choice == '3':
                file_manager.go_to_parent_directory()
            
            elif choice == '4':
                file_manager.display_directory_contents()
                indices = input("Enter file indices to select (comma-separated): ")
                file_manager.file_selector.select_files_by_indices(indices, file_manager.current_path)
            
            elif choice == '5':
                dest = input("Enter destination path for copying: ")
                file_manager.copy_files(dest)
            
            elif choice == '6':
                dest = input("Enter destination path for moving: ")
                file_manager.move_files(dest)
            
            elif choice == '7':
                file_manager.delete_files()
            
            elif choice == '8':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()