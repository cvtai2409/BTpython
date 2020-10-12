def input_data(n):
    arr=[]
    for i in range(n):
        x = int(input(f"Input item[{i}]: "))
        arr.append()
    return arr

def input_list(n):
    arr = []
    i = 0
    while True:
        x = input(f"Input item[{i}]: ")
        try:
            arr.append(int(x))
            i += 1
            if i >= n:
                break
        except:
            print("Chưa nhập đúng số nguyên. Nhập lại!")
    return arr

def tinh_tong(n):
    n=input_list(n)
    tong = 0
    for i in n:
        tong+=i
    return tong

def tinh_tich(n):
    n=input_list(n)
    tich = 1
    for i in n:
        tich*=i
    return tich

def tim_max(n):
    n=input_list(n)
    max = n[0]
    for i in range(1,len(n)):
        if(max<n[i]):
            max=n[i]
    return max

def tim_min(n):
    n=input_list(n)
    min = n[0]
    for i in range(1,len(n)):
        if(min>n[i]):
            min=n[i]
    return min

def so_le(n):
    n=input_list(n)
    result = []
    for i in n:
        if(i%2!=0 & i%2==0):
            result.append(i)
        return result

def so_chan(n):
    n=input_list(n)
    result = []
    for i in n:
        if(i%2==0):
            result.append(i)
        return result

def kiem_tra_snt(n):
    n=input_list(n)
    count = 0 
    for i in range(1, len(n)):
        if (n%i== 0):
            count +=1
    if count == 2:
        return True
    return False



n=int(input("Nhap: "))
# print(input_list(n))
# print(tinh_tong(n))
# print(tinh_tich(n))
# print(tim_max(n))
# print(tim_min(n))
print(so_le(n))
print(so_chan(n))
# print(kiem_tra_snt(n))