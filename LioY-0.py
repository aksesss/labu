def main():
  array1 = [5,5,3,4,5,6,7,8]
  array2 = [2,3,4,5,6,7, 0]
  string = "qwerty"
  print("min =", find_min(array1))
  print ("average =", average(array1))

  print("min =", find_min(array2))
  print ("average =", average(array2))
  
  print("replaced = ", perevorot(string))
  
  ivan = {
  "name": "ivan",
  "age": 34,
  "children": [{
    "name": "vasja",
    "age": 19,
  },{
    "name": "petja",
    "age": 12,
  }]
        } 

  darja = {
  "name": "darja",
  "age": 41,
  "children": [{
    "name": "kirill",
    "age": 21,
  },{
    "name": "pavel",
    "age": 15,
  }]
        } 

  emps = [ivan, darja]
  
  find(emps)


def find_min(massiv):
  min_value = massiv[0]
  for value in massiv:
    if value <= min_value:
      min = value
  return min


def average(massiv):
  sum = 0;
  for value in massiv:
    sum += value
    average_value = sum/len(massiv)
  return average_value


def perevorot(ssting):
  result_string = ""
  length_of_str = len(ssting)  
  while length_of_str != 0:
    length_of_str -= 1
    result_string = result_string + ssting[length_of_str]
  return result_string
  

def find(employer_mass):
  for empl in employer_mass:
    for child in empl["children"]:
      if child["age"] >= 18:
        print (empl["name"])
        break
  return 0

  
main()