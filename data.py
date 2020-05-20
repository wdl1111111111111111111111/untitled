
one=[]
two=[]
three=[]
a='D:\\1.txt'
def demo():
    with open(a) as jaf:
        data = jaf.readlines() #读取数据行
        for datas in data:
            james = datas.strip().split('_')#将数据转换为列表
            m=james[0]+","+james[1]
            k=james[2]+","+james[3]
            n=james[4]+","+james[5]
            one.append(m)
            two.append(k)
            three.append(n)
            # print(m,k,n)
            #print(k)
        return one,two,three

