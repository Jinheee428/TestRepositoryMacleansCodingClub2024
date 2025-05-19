stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
count = sum(1 for s in stringsList if s[0].lower() == s[-1].lower())
print(count)
