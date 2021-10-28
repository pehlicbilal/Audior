
def openfiles(fname):
    f = open(f"uploaded_files/{fname}.txt", "r")
    reedFiles = f.read()
    return reedFiles
