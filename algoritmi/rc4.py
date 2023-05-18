def ksa(key):
    schedule=[i for i in range(0,256)]

    #Cream un array temporar pentru a avea un initial permutation pentru schedule
    t=[]
    for k in range(0,256):
        t.append(key[k%len(key)])

    i=0
    for j in range(0,256):
        i=(i+schedule[j]+t[j])%256
        schedule[i],schedule[j]=schedule[j],schedule[i]

    return schedule

def create_stream():
    stream[]

print(ksa([2,3,4]))