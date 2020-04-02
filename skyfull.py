# A fun Program
def pattern(string):
    store = []
    temp = ''
    for i in string:
        temp+=i
        if i != ' ':
            store(temp)
            print(temp)
    store.reverse()
    for j in store[1:]:
        print(j)        