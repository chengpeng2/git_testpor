import yaml
import os

def get_token(yamName="token.yaml"):
    #获取当前脚本所在的文件夹路径
    base_path = os.path.dirname(os.path.relpath(__file__))
    #获取yaml文件路径
    yamlPath=os.path.join(base_path,'token.yaml')
    #open方法打开读取
    with open(yamlPath,'r',encoding='utf-8') as f:
        a=yaml.load(f,Loader=yaml.FullLoader)
       # print(a['token'])
    return a['token']
if __name__ =='__main__':
    print(get_token())