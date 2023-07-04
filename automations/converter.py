from PIL import Image
from fileoperations import FileOperations

class PNGConverter:
    def __init__(self) -> None:
        pass

    def convert_pngA_bit_to_bit(self, imagepath: str, newimagepath: str, filetype: str, tobit: int) -> str:
        '''
        converts an image to a new image with a different bit depth
        the images are png with alpha channel going in and out
        params:
            imagepath: str, specifies the image to convert
            newimagepath: str, specifies the new image
            filetype: str, specifies the filetype
            tobit: int, specifies the new bit depth
        returns a list of messages
        '''
        message =""
        try:
            img = Image.open(imagepath)
            # conversion of image to new bit depth with alpha channel
            img.convert("RGBA",palette=Image.ADAPTIVE, colors=256)
            img.save(newimagepath, filetype, bitspersample=tobit)
            message = ("Converted: ", imagepath, " to: ", newimagepath)
        except Exception as e:
            message = ("Error: ", e)
        return message

if __name__ == "__main__":
    c = PNGConverter()
    fo = FileOperations()
    files_and_folders = fo.get_all_files_and_folders("I:/OneDrive/Desktop/Neuer Ordner")
    files = fo.get_files_with_types(files_and_folders, ".png")
    print(files)
    for file in files:
        fname = "I:/OneDrive/Desktop/Neuer Ordner/"+file
        print(c.convert_pngA_bit_to_bit(fname, fname, "PNG", 8))
        

