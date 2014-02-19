numbers = "zero one two three four five six seven eight nine".split()
numbers.extend("ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())
numbers.extend(tens if ones == "zero" else (tens + ones) \
                for tens in "twenty thirty forty fifty sixty seventy eighty ninety".split() \
                for ones in numbers[0:10])
numbers.extend((ones + "hundred") if tens == "zero" else (ones + "hundredand" + tens) \
                for ones in numbers[1:10] \
                for tens in numbers[0:100])
numbers.extend(["onethousand"])

print len("".join(numbers[1:1001]))