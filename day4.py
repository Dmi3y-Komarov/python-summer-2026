print("#1")

student = {
        "name" : "Oleg",
        "age" : 20,
        "city" : "Orsk"
        }
print(student)
print(f"Oleg,s age is {student["age"]}")

print("#2")

student["age"] = 21
print(f"Oleg,s age is {student["age"]}")

print("#3")

student["speciality"] = "automation"
print(student)

print("#4")

for key, value in student.items():
    print(key, value)

print("#5")

names = ["Oleg", "Ivan", "Alex"]
points = [10, 20, 30, 10]

results = {}

for key, value in zip(names, points):
    results[key] = value
print(results)
