import pymongo
con=pymongo.MongoClient("mongodb+srv://kamalesh:kamalesh3012@cluster0.kdaisi3.mongodb.net/?retryWrites=true&w=majority")
print("connection successfully")
db=con["chocalatecafe"]
print("db created successfully")
col=db["chocalate store"]
print("collection of chocalate details created successfully")
mychoc=[{"name":"diarymilk","quantity":20,"price":10},
        {"name":"kitkat","quantity":10,"price":5},
        {"name":"darkchocalte","quanity":5,"price":10},
        {"name":"5star","quantity":15,"price":20}]
x=col.insert_many(mychoc)
##print(x.inserted_ids)
print('welocme to shop sir')
##sales=str(input("what you want"))
for i in col.find({},{"_id":0}):
    print(i)
print("we have collection of choclate")
sales=str(input("what you want"))
if col.find_one({"name":sales}):
    print('yes sir it is avaible')
    a=int(input("pls tell me how many choc want"))
    c=a*col.find_one({"name":sales})["price"]
    print(c)

            



