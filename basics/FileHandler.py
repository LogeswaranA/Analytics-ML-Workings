

class FileManager:

    def __init__(self,filename,mode ):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_value,traceback):
        print("exc_value",exc_value)
        if self.file:
            self.file.close()


with FileManager("Example.txt","w") as f:
    f.write("Hey Man")