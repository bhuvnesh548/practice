s = "   Hello   , Python   !"

print((s.strip()))# print(s.strip())        # "Hello, Python!"  — remove spaces
print(s.lower())# print(s.lower())        # "  hello, python!  "
print(s.upper())# print(s.upper())        # "  HELLO, PYTHON!  "
print(s.title())# print(s.title())        # "  Hello, Python!  "
print(s.replace("bhuvnesh","pandey"))# print(s.replace("Python", "World"))  # replace substring
print(s.split("|"))# print(s.split(","))      # ['  Hello', ' Python!  ']
print("|".join(["A","B"]))# print(",".join(["a","b","c"]))  # "a,b,c"
# print(s.find("Python"))  # index of first match
# print(s.startswith("  H"))  # True
# print(s.endswith("!  "))    # True
# print(s.count("l"))      # 2
# print("42".isdigit())   # True
# print("abc".isalpha())  # True