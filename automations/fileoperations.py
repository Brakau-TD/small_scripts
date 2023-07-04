from userinterface import UserInterface
import shutil
import os

class FileOperations:
    def __init__(self) -> None:
        pass

    def create_specific_folders(self,folderpath: str,folderlist: str) -> list:
        '''
        creates folders in a specific folderpath
        params:
            folderpath: str
            folderlist: list
        returns a list of messages
        '''
        messages = []
        for folder in folderlist:
            if not os.path.exists(folderpath+folder):
                os.mkdir(folderpath+folder)
                messages.append("Created: ", folderpath+folder)
            else:
                messages.append("Folder: ", folderpath+folder, " already exists.")
        return messages
    
    def get_all_files_and_folders(self, basefolder: str = "C://") -> list:
        '''
        returns all files and folders in a specific folder
        params:
            basefolder: str, default: "C://"
        returns a list of files and folders
        '''
        return os.listdir(basefolder)
    
    def get_only_folders(self, dircontent: list, basefolder: str) -> list:
        '''
        returns only folders from a specific folder
        params:
            dircontent: list of files and folders in a specific location
            basefolder: str, specifies the location
        returns a list of folders
        '''
        folders = []
        for item in dircontent:
            if "." in item:
                pass
            elif item[0] == "$" or item[0] == "~" or item[0] == "_":
                pass
            elif item.startswith("zip"):
                pass
            else:
                folders.append(basefolder+item+"/")
        return folders
        
    def move_filetypes_to_new_folder(self, folderlist: list, filetype: str|list, destinationfolder: str)->str:
        '''
        moves files with a specific filetype (str) or filetypes (list) to a new folder
        params:
            folderlist: list of folders
            filetype: str or list of filetypes
            destinationfolder: str, specifies the destination folder
        returns a confirmation message: str
        '''
        counter = 0
        if type(filetype) == str:
            filetype = [filetype]   
        for folder in folderlist:
            alltypes = os.listdir(folder)
            for file in self.get_files_with_types(alltypes, filetype):
                counter += 1
                self.move_file_to_folder(f'{folder}{file}', destinationfolder)
        return f'Moved {counter} files to {destinationfolder}'

    def get_files_with_types(self, filedump: list, filetypes: list) -> list:
        '''
        returns files with specific filetypes
        params:
            filedump: list of files
            filetypes: list of filetypes
        returns a list of files with specific filetypes
        '''
        files = []
        for file in filedump:
            for filetype in filetypes:
                if file.endswith(filetype):
                    files.append(file)
        return files

    def move_file_to_folder(self, file: str, folder: str) -> str:
        '''
        moves a file to a specific folder
        params:
            file: str, specifies the file
            folder: str, specifies the destination folder
        returns a confirmation message
        '''
        try:
            shutil.move(file, folder)
        except shutil.Error as e:
            print(e)
        return f'Moved {file} to {folder}'
    
    def delete_empty_folders(self, folderlist: list) -> list:
        '''
        IMPORTANT: this deletes bypassing the recycle bin, so folders are deleted permanently
        deletes empty folders
        params:
            folderlist: list of folders
        returns a list of errors or a confirmation message
        '''
        errorlist = []
        for folder in folderlist:
            try:
                os.rmdir(folder)
            except OSError as e:
                errorlist.append(e)
        return errorlist if len(errorlist) > 0 else ["No errors"]
    
    def delete_filetypes(self, folderlist: list, filetype: str) -> str:
        '''
        IMPORTANT: this deletes bypassing the recycle bin, so files are deleted permanently
        deletes files with a specific filetype from a list of folders
        params:
            folderlist: list of folders
            filetype: str, specifies the filetype
        returns a confirmation message
        '''
        removallist = []
        for folder in folderlist:
            for file in os.listdir(folder):
                if file.endswith(filetype):
                    os.remove(folder+file)
                    removallist.append(folder+file)
        return f'Removed {len(removallist)} files with type {filetype}' if len(removallist) > 0 else f'No files with type {filetype} found in {folderlist}'
    
    def delete_filenames(self, folderlist: list, filename: str) -> str:
        '''
        IMPORTANT: this deletes bypassing the recycle bin, so files are deleted permanently
        deletes files with a specific filename from a list of folders
        params:
            folderlist: list of folders
            filename: str, specifies the filename
        returns a confirmation message
        '''
        deletedfiles = []
        for folder in folderlist:
            for file in os.listdir(folder):
                if file == filename:
                    os.remove(folder+file)
                    deletedfiles.append(folder+file)
        return f"Removed: {folder+file}" if len(deletedfiles) > 0 else "No files removed"

        
def main() -> None:
    fo=FileOperations()
    ui = UserInterface()
    basefolder = "H:/Bilder/"
    orffolder = "H:/Bilder/Orfs/"
    dircontent = fo.get_all_files_and_folders(basefolder)
    folderlist = fo.get_folders(dircontent, basefolder)
    # print([x for x in folderlist])
    fo.move_filetypes_to_new_folder(folderlist, ".JPG")
    # fo.delete_filetypes(folderlist, ".tmp")
    #fo.delete_filenames(folderlist, "temp")
    fo.delete_empty_folders(folderlist)

if __name__ == "__main__":
    main()

