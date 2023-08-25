from distutils.util import strtobool
import os
import pickle
from pathlib import Path
import sys

print()
modelPath="..\\..\\workspace\\model\\"
DFLModelOptionF = ""
if len(sys.argv) < 2:
    # print("Error! need a model file name!")
    # sys.exit(-1)
    i=1
    m={}
    for filename in os.listdir(modelPath):
        # print("["+filename+"]")
        if filename.endswith(".dat"):
            m[str(i)]=filename
            # print(i," = "+m[i])
            i=i+1
    
    if len(m) == 0:
        print("no model option file found, quit.")
        sys.exit(-1)

    print("!!! Please backup your model first !!!")
    print("!!! Please backup your model first !!!")
    print("!!! Please backup your model first !!!")
    print()
    print("Select a model option file to view/edit:")
    print()
    for lm in m:
        print(lm+" = "+m[lm])
    print()

    key = input("Please input ID: ")
    print()
    if not key in m:
        print("not a choice, quit.")
        sys.exit(-1)

    DFLModelOptionF = os.path.abspath(modelPath+m[key])

else:
    DFLModelOptionF = os.path.abspath(modelPath+sys.argv[1])

if not Path(DFLModelOptionF).exists:
    print("Error! model file is not found!")
    sys.exit(-1)

MContent = Path(DFLModelOptionF).read_bytes()
MOption = pickle.loads(MContent)

isModified = False

while True:
    # 打印全部参数，格式不易查看
    # print(MOption['options'])

    # 分行逐个打印参数。
    os.system('cls') 
    print("*** ["+DFLModelOptionF+"] ***")
    print("*** List Params in this model start ***")
    print()
    for oneOp in MOption['options']:
        print(str(oneOp).ljust(25), "=" , str(MOption['options'][oneOp]).ljust(15), type(MOption['options'][oneOp]))
    print()
    print("*** List Params in this model end ***")
    print()

    key=''
    print("Input a existing param name to modify. or a new param name to add. Input 'quit' to save quit.")
    print("then input param value, if ' ' means to delete.")
    print()
    key = input("Please input param name: ")
    if key == 'quit' or key =='\26':
        break
    else:
        content = input("Please input param value: ")
        print()
    if content == ' ':
        del MOption['options'][key]
        isModified = True
    else:
        try:
            intcontent = int(content)
            MOption['options'][key] = intcontent
            print(key+" is set to INTEGER value =",intcontent)
            input()
        except:
            try:
                fcontent = float(content)
                MOption['options'][key] = fcontent
                print(key+" is set to FLOAT value =",fcontent)
                input()
            except:
                try:
                    bcontent = bool(strtobool(content))
                    MOption['options'][key] = bcontent
                    print(key+" is set to BOOL value =",bcontent)
                    input()
                except:
                    MOption['options'][key] = content
                    print(key+" is set to STRING value =",content)
                    input()
        isModified = True

if isModified:
    print("now saving...")
    Path(DFLModelOptionF).write_bytes(pickle.dumps(MOption))
else:
    print("leaving without any change.")
print()


