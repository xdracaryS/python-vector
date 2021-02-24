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
        oldType = type(self.get_last_data())
        if oldType != None:
            if type(data) != oldType:
                return
        self.v_data.append(data)
    def insert(self, index, data):
        if index < 0 or index > len(self.v_data):
            return
        oldType = type(self.get_last_data())
        if oldType != None:
            if type(data) != oldType:
                return
        self.v_data.insert(index,data)


