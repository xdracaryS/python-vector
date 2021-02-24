# python-vector

Hi this class vector python version...

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
