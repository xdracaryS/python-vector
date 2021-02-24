import os


class vector(object):
    def __init__(self):
        self.v_data=[]
    def __del__(self):
        self.v_data=[]
    def destroy(self):
        self.clear()
    def clear(self):
        self.v_data.clear()
    def __getitem__(self, key):
       return self.at(key)
    def __setitem__(self, key, data):
        try:
            self.v_data[key] = data
        except:
            pass
    def data(self):
        return self.v_data
    def size(self):
        return self.__len__()
    def erase(self,key):
        try:
            del self.v_data[key]
        except:
            pass
    def swap(self, vector):
        data = self.v_data
        new_data = vector
        self.v_data=new_data
        return data
    def front(self):
        try:
            return self.v_data[0]
        except:
            return None
    def __len__(self):
        return len(self.v_data)
    def last(self):
        return self.get_last_data()
    def resize(self, size):
        self.v_data = [0] * (size)
    def at(self, key):
        try:
            return self.v_data[key]
        except:
            return None
    def get_last_data(self):
        try:
            return self.v_data[len(self.v_data)-1]
        except:
            return None
    def pop_back(self):
        try:
            del self.v_data[len(self.v_data)-1]
        except:
            pass
    def push_back(self, data):
        if data in self.v_data:
            return
        if len(self.v_data)!=0:
            if type(data) != type(self.get_last_data()):
                return
        self.v_data.append(data)
    def insert(self, index, data):
        if index < 0 or index > len(self.v_data):
            return
        self.v_data.insert(index,data)

teststring = vector()
teststring.push_back("Ahmet")
teststring.push_back("Muzaffer")
teststring.push_back("Yusuf")
teststring.push_back("Elif")
teststring.push_back("Murat")
teststring.push_back("Hakan")

print teststring.data() # ['Ahmet', 'Muzaffer', 'Yusuf', 'Elif', 'Murat', 'Hakan']

teststring.insert(3,"dracaryS")

print teststring.data() # ['Ahmet', 'Muzaffer', 'Yusuf', 'dracaryS', 'Elif', 'Murat', 'Hakan']

print len(teststring) # 6

teststring.pop_back()

print teststring.data() # ['Ahmet', 'Muzaffer', 'Yusuf', 'dracaryS', 'Elif', 'Murat']

print len(teststring) # 5

print teststring.at(1) # Muzaffer

print teststring.front() # Ahmet

print teststring.last() # Murat

teststring[3] = "dracaryS-New"

print teststring.at(3) # dracaryS-New

teststring.erase(3)

print teststring.data() # ['Ahmet', 'Muzaffer', 'Yusuf', 'Elif', 'Murat']

######################################################################################

testint = vector()
testint.push_back(10)
testint.push_back(20)
testint.push_back(30)
testint.push_back(40)
testint.push_back(50)

print testint.data() # [10, 20, 30, 40, 50]

testint.insert(3,13)

print testint.data() # [10, 20, 30, 13, 40, 50]

print len(testint) # 6

testint.pop_back()

print testint.data() # [10, 20, 30, 13, 40]

print len(testint) # 5

print testint.at(1) # 20

print testint.front() # 10

print testint.last() # 40

testint[3] = "3413"

print testint.at(3) # 3413

testint.erase(3)

print testint.data() # [10, 20, 30, 40]

os.system("pause")

