print("Hello World!")

int_variable = 1
string_variable = "Hi"

int_list = [1, 2, 3]
string_list = ["Hi", "there"]

if int_variable in range(1, 4):
    print("The variable was equal to 1")
elif int_variable in range(2, 5):
    print("The variable was equal to 2")
else:
    print("The variable was neither 1 nor 2")

if int_variable in range(1, 4):
    print("The variable was equal to 1")
if int_variable in range(2, 5):
    print("The variable was equal to 2")
else:
    print("The variable was neither 1 nor 2")

while int_variable < 3:
    print("int_variable", int_variable)
    int_variable += 1

for i in range(10):
    print("The counter is", i)

for i in string_list:
    print("Printing the string:", i)


def multiply_by_2_and_add_4(x):
    return (x * 2) + 4


why_we_use_variables = 6
result = multiply_by_2_and_add_4(why_we_use_variables)
print(f"The result of multiplying {why_we_use_variables} by 2 and adding 4 is", result)

math = 1 + 2 - 3 * 4 / 5 // 6 ** 7 % 8

s = "This is a long string..."
print("Split:", s.split())
print("Sort:", s.upper())
print("Join:", "$$$".join(string_list))
