"""

"""


def minimumBags(strength, items):
    item_count = {}
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    total_bags = 0
    for item in item_count.items():
        item_total = item[1]
        while item_total > 0:
            item_total -= strength
            total_bags += 1
    return total_bags


test_strength = 2
test_items = ["DAIRY",
              "DAIRY",
              "PRODUCE",
              "PRODUCE",
              "PRODUCE",
              "MEAT"]
print(minimumBags(test_strength, test_items))
test_strength = 3
test_items = ["DAIRY",
              "DAIRY",
              "PRODUCE",
              "PRODUCE",
              "PRODUCE",
              "MEAT"]
print(minimumBags(test_strength, test_items))
test_strength = 10
test_items = []
print(minimumBags(test_strength, test_items))
test_strength = 5
test_items = ["CANNED", "CANNED", "PRODUCE",
              "DAIRY", "MEAT", "BREAD",
              "HOUSEHOLD", "PRODUCE", "FROZEN",
              "PRODUCE", "DAIRY"]
print(minimumBags(test_strength, test_items))
test_strength = 2
test_items = ["CANNED", "CANNED", "PRODUCE",
              "DAIRY", "MEAT", "BREAD",
              "HOUSEHOLD", "PRODUCE", "FROZEN",
              "PRODUCE", "DAIRY"]
print(minimumBags(test_strength, test_items))
