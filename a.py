from datetime import datetime
word="ABCDEFGHIJKLNMOPQRSTUVWXYZ"
def getcode(id):
    id=str(id)
    if len(id) != 4:
        return "ERROR"
    currentDateAndTime = datetime.now()
    min=str(currentDateAndTime.minute)
    sec=str(currentDateAndTime.second)
    if len(min) == 1:
        min="0"+min
    if len(sec) == 1:
        sec="0"+sec
    sec=sec[0],sec[1]
    code=[]
    for i in range(4):
        code.append(word[int(id[i])+int(sec[1])])
    for i in range(2):
        code.append(word[int(min[i])+int(sec[1])])
    code.append(word[int(sec[0])])
    code.append(word[int(sec[1])])

    return "".join(code)
def validate(code):
    idlist=["1234","4321","1207"]
    if len(code) != 8:
        return "无效的验证码"
    decode=[]
    
    for i in range(8):
        decode.append(str(word.index(code[i])))
    for i in range(6):
        decode[i]=str(int(decode[i])-int(decode[-1]))
    
    currentDateAndTime = datetime.now()
    decode = "".join(decode)
    print(decode[0:3])

    if int(decode[4:6]) != int(currentDateAndTime.minute):
        return "超时的验证码"
    if decode[0:4] not in idlist:
        return "无效的id"
    return "通过"

    
    

    
        
