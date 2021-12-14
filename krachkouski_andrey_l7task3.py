import os, shutil

def clone(src, dst):
    if (0 == src.lower().find(dst.lower())):
        return
    for f in os.listdir(src):
        path = os.path.join(src, f)
        if (os.path.isdir(path)):
            clone(path, dst)
        else:
            pathdet = os.path.split(src)
            if (-1 < pathdet[0].find("templates")):
                destfolder = os.path.join(dst, pathdet[1])
                if (not os.path.exists(destfolder)):
                    os.makedirs(destfolder)
                shutil.copy(path, os.path.join(destfolder, f))

def templater(folder):
    clone(folder, os.path.join(folder, "templates"))

templater("my_project")