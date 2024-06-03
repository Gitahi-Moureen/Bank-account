def hello(name):
    print( f"Hello {name}")

def year_of_birth(name,age):
    print(f"Hello {name} you were born in {2024-age}")



def my_country(country="Uganda"):
    print(f"Hello Akirachix from {country}")

def greet(*names):
    for name in names:
         print(f"hello {name}")

def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word 
        sentence += " "
    return sentence   

def sum_and_greet(*args,**kwargs):
    total = 0
    for x in args:
        total += x
    f = kwargs["first_name"]
    l = kwargs["last_name"]
    greeting = f"Hello {f} {l} the sum of your numbers is {total}"


    return greeting               



students = [{"age":19,"name":"Eunice"},
            {"age":21,"name":"Amanda"},
             {"age":20,"name":"Asha"}]
def greetings(*args,**kwargs):
    l = 2024 - student.age
    f = kwargs["first_name"]
    greeting = f"Hello {f} you were born in the year {l}"
    return greeting