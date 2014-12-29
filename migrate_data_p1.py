import os
import tempfile
import zipfile
import shutil


def get_all_ext(ext, path):
    zip_files = []
    for (dir, subdirs, files) in os.walk(path):
        zip_files += [os.path.join(dir, f) for f in files if f.endswith(ext)]
    return zip_files


def extract_zip(zipname):
    tempdir = tempfile.mkdtemp()
    zipf = zipfile.ZipFile(zipname, 'r')
    zipf.extractall(tempdir)
    return tempdir


def replace_colons_file(path):
    text = open(path, "r").read()
    text = text.replace("::", "/")
    open(path, "w").write(text)


def replace_colons(path):
    jsf = get_all_ext(".js", path)
    for f in jsf:
        replace_colons_file(f)


def do_work():
    zips = get_all_ext(".zip", ".")
    for z in zips:
        print "process: " + z
        tempdir = extract_zip(z)
        replace_colons(tempdir)
        shutil.make_archive(z[:-4], 'zip', tempdir)
        shutil.rmtree(tempdir)


if __name__ == '__main__':
    do_work()