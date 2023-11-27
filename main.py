# imports 
from pathlib import Path
import os
import shutil

# intialising path
def initialise_download_path():
    with open("./download_path.txt") as f:
        download_path = f.readlines()[0]
        return download_path

# main function
def main():
    download_path = initialise_download_path()
    # extensions
    img_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    exe_extensions = [".exe", ".msi"]
    doc_extensions = [".doc", ".docx", ".csv", ".xlsx", ".ppt", ".pptx", ".txt", ".pdf"]
    arc_extensions = [".zip", ".rar"]

    while True:
        files = os.listdir(download_path)
        for f in files:
            print(f"one {f}")
            # checking if it is a chrome download
            if f.endswith(".crdownload") or Path(f).suffix == "":
                continue
            else:
                ext = Path(f).suffix
                # checking if which category the file belongs to
                if ext in img_extensions:
                    old_path = os.path.join(download_path, f)
                    new_path = os.path.join(download_path, "Images", f)
                    shutil.move(old_path, new_path)
                    
                elif ext in exe_extensions:
                    old_path = os.path.join(download_path, f)
                    new_path = os.path.join(download_path, "EXEs", f)
                    shutil.move(old_path, new_path)

                elif ext in doc_extensions:
                    print(f)
                    old_path = os.path.join(download_path, f)
                    new_path = os.path.join(download_path, "Documents", f)
                    shutil.move(old_path, new_path)

                elif ext in arc_extensions:
                    old_path = os.path.join(download_path, f)
                    new_path = os.path.join(download_path, "Archives", f)
                    shutil.move(old_path, new_path)

                else:
                    old_path = os.path.join(download_path, f)
                    new_path = os.path.join(download_path, "Others", f)
                    shutil.move(old_path, new_path)


if __name__ == '__main__':
    main()