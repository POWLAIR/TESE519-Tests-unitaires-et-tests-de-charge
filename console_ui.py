from file_system import FileSystem
from file_explorer import FileExplorer
from file_selector import FileSelector
from file_manager import FileManager

def main_menu():
    file_system = FileSystem()
    file_explorer = FileExplorer()
    file_selector = FileSelector()
    file_manager = FileManager(file_system, file_explorer, file_selector)
    
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
                contents = file_manager.display_directory_contents()
                for index, element in enumerate(contents):
                    element_type = "📁 Folder" if file_explorer.is_directory(element) else "📄 File"
                    print(f"{index}. {element_type}: {element}")
            
            elif choice == '2':
                index = int(input("Enter navigation index: "))
                file_manager.navigate(index)
            
            elif choice == '3':
                file_manager.go_to_parent_directory()
            
            elif choice == '4':
                contents = file_manager.display_directory_contents()
                for index, element in enumerate(contents):
                    element_type = "📁 Folder" if file_explorer.is_directory(element) else "📄 File"
                    print(f"{index}. {element_type}: {element}")
                indices = input("Enter file indices to select (comma-separated): ")
                file_selector.select_files_by_indices(indices, file_explorer.get_current_path())
            
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