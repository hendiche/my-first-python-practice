monthConversions = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "nov",
    "dec": "december",
    1: "number 1",
    2: "number 2",
}

print(monthConversions['jan'])
print(monthConversions.get("jan"))
print(monthConversions.get("gab", "not a valid key"))
print(monthConversions.get(1))
