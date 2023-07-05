class StructureOperations:
    def __init__(self, fileoperations) -> None:
        self.dircontent = None
        self.fileoperations = fileoperations

    def read_folder(self, basefolder: str = "C://"):
        self.dircontent = self.fileoperations.get_all_files_and_folders(basefolder)
        return self.dircontent

    def get_folders(self, basefolder: str = "C://") -> list:
        self.read_folder(basefolder)
        return self.fileoperations.get_only_folders(self.dircontent, basefolder)

    def list_entries(self, dircontent: list) -> list:
        self.fileoperations
