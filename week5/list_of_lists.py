breakfast = ["Lucky Charms", "waffles", "english muffin"]
lunch = ["panini", "pizza", "salad"]
dinner = ["two pieces of chicken with rice and teryaki and onion",
          "pasta with meatballs",
          "burrito"]

allfood = breakfast + lunch + dinner
print(allfood)
print(allfood[2])

print("\n")

allfood_better = [breakfast, lunch, dinner]
print(allfood_better)
print(allfood_better[2])
print(allfood_better[0][2])


for sublist in allfood_better:
    for e in sublist:
        print(e, end=" ")
    print("\n")

