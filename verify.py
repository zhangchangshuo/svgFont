from myConfig import *
from myUtils import *
from extract import *
import os

cwd=os.getcwd()
os.chdir(ff_work_directory)
import fontforge
os.chdir(cwd)

def verify():
    key_digest = getDigest(key)
    key_len=len(key_digest)

    sign = ["?" for i in range(key_len)]
    F = fontforge.open(verify_font_path)
    for name in F:
        index=str(F[name].unicode)
        width=str(F[name].width)
        filename = index+'_'+name+'_'+width+'.'+ext
        F[name].export(svg_ver_path+'/'+filename)
        result = oneByoneGetAllSign(sign,filename)
        if result == -1:
            continue
        if type(result) == type('str'):
            break
    if key_digest == result:
        print('Verify successfully! '+" Digest is "+result)
        return True
    else:
        print('Fail to Verify',result)
        return False

if __name__ == '__main__':
    verify()