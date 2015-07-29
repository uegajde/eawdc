import hashlib
import os


def removerepeatedfiles(path):
    print ("repeatfileremover : removing repeated files")
    delfiles = 0
    hash = []
    for tops, dirs, files in os.walk(path):
        for f in files:
            filepath = os.path.join(tops, f)
            checkingfile = open(filepath, 'rb')
            buf = checkingfile.read()
            checkingfile.close()
            hasher = hashlib.md5()
            hasher.update(buf)
            newhash = hasher.hexdigest()
            
            vailed = 1
            for vailedhash in hash:
                if vailedhash == newhash:
                    vailed = 0
                    break
            if vailed == 1:
                hash.append(newhash)
            elif vailed == 0:
                delfiles += 1
                os.remove(filepath)
    print ("repeatfileremover : remove",delfiles,"repeated files")
    return