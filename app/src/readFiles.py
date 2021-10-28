
def openfiles(fname):
    f = open(f"uploaded_files/{fname}", "r")
    reedFiles = f.read()
    return reedFiles
