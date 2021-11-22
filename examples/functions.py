# FUNCTION TO SQUARE NUMBERS
def square(x):
    return x*x


# PRINTING ONE SQUARE
print(square(5)) # 25

# PRINTING NUMBER AND ITS SQUARE IN RANGE OF 10
for i in range(10):
    print(f"The square of {i} is {square(i)}")
