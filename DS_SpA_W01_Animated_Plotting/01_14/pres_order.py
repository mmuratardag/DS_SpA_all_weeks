import random
random.seed(42)
names = [
    "alexandra",
    "alphan",
    "anastasia",
    "bala",
    "galiya",
    "krystana",
    "lena",
    "mahmoud",
    "murat",
    "müfit",
    "nader",
    "pavel",
    "pietro",
    "pooja",
    "svenja",
]
random.shuffle(names)
for i, name in enumerate(names):
    if i == len(names) // 2 + 1:
        print("---BREAK---")
    print(f"{i + 1}. {name}")


"""
1. murat
2. pooja
3. mahmoud
4. lena
5. svenja
6. pietro
7. krystana
8. anastasia
---BREAK---
9. müfit
10. bala
11. galiya
12. pavel
13. alexandra
14. alphan
15. nader
"""
