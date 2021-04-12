a = 0;
S = 0;
for x in range(0,4,1):
    ya = input("Number please...");
    ya = int(ya);
    S = S + ya;
    S = str(S);
    ya = str(ya);
    print(str("The user input is:"+ya+" The current sum is:"+S));
    S = int(S);
    ya = int(ya);
S = int(S);
a = S / 4;
a = str(a);
print("The average is: " +a);
