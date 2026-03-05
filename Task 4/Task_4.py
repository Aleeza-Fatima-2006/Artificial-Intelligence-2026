og_num = 5893804115457289
a = og_num % 10
og_num = og_num // 10
print("After removing last digit:", og_num)
og_num1 = int(str(og_num)[::-1])
print("Reversed number:", og_num1)
og_num2 = str(og_num1)
total = 0
for i in range(len(og_num2)):
    digit = int(og_num2[i])
    if i % 2 == 0:
        digit *= 2
        if digit > 9:
            digit -= 9
    print(digit, end=" ")
    total += digit
total += a
print("\nTotal sum:", total)
if total % 10 == 0:
    print("Valid card number")
else:
    print("Invalid card number")