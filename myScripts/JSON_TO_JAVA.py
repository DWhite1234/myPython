import sys
sys.path.append("..")
import json
import logging as log
from config.logConfig import logfile_path,log


#读取json文件
url = '/Users/zhongtao/disk/workspace/mine/myPython/test/demo.json'
with open(url,'r+') as f:
    data= json.load(f)

#类型判断
def typeDetermine(data):
    if isinstance(data, str):
        return "String"
    elif isinstance(data, int):
        return "Integer"
    elif isinstance(data,float):
        return "BigDecimal";
    elif isinstance(data,list):
        first = list[0]
        return "List<"+typeDetermine(first)+">"
    else :
        log.info("无法判断的类型,默认赋值Object,请手动修改!")
        return "Object"


#驼峰转换
def transferName(keyWord:str):
    if keyWord.__contains__("_"):
        i = keyWord.index("_")
        return keyWord[:i]+keyWord[i+1:i+2].upper()+keyWord[i+2:]
    else:
        return keyWord


wf = open('./demo.java','a');
wf.writelines("@Data\n")
wf.writelines("public class demo{\n")
for k in data:
    wf.writelines("    private "+typeDetermine(data[k])+" "+transferName(k)+"\n");
wf.writelines("}")


