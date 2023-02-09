movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# 1
def imdb1(name):
     for i in movies: 
        if i['name'] == name: 
            if float(i['imdb']) >  5.5:  
                return True 
            else: 
                return False 
print(imdb1("We Two"))
# 2
def imdb2(lis):
    li1 = []
    for i in lis: 
        if imdb1(i["name"]):
            li1.append(i["name"])
    return li1
print(imdb2(movies)) 
# 3
def category(category):
    li1 = []
    for i in movies: 
        if i['category'] == category:
            li1.append(i["name"])
    return li1
print(category("Thriller"))
# 4
def average(lis):
    sum = 0
    for i in lis:
        sum += i['imdb']
    return sum/len(lis)
print(average(movies))
# 5
def cateaverg(category):
    li2=[]
    sum=0
    for i in movies:
        if i['category'] == category:
            sum+=i['imdb']
    return sum/len(movies)
print(cateaverg("Thriller"))