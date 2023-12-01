list_of_cloud = [ "aws ", "azure ", "oracle"]
list_of_env = ["dev","prod","test"]
print(list_of_cloud)



# list_of_cloud = [ "aws ", "azure ", "oracle"]
# list_of_env = ["dev","prod","test"]
# print(list_of_cloud[0])


# list_of_cloud = [ "aws ", "azure ", "oracle"]
# list_of_env = ["dev","prod","test"]
# print(list_of_cloud[1])


# list_of_cloud = [ "aws ", "azure ", "oracle"]
# list_of_env = ["dev","prod","test"]
# print(list_of_cloud[2])


for i in range(10):
    print(i)
    
# Example:
for i in range(10):
    print("Hit-man") 

# Dictionary
dict_of_cloud = {
       "aws":"Amazon web services",
        "azure":"Microsoft azure",
        "oracle":"oracle cloud"
 } 
print(dict_of_cloud["aws"])
print(dict_of_cloud.get("azure"))

# adding or update
dict_of_cloud.update({"linode":"linode cloud"})
print (dict_of_cloud)