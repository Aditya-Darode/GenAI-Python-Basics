import re
text = "The quick brown fox jumps over the lazy dogs."

#Search for a pattern
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found")
#     print("Start index:", match.start())
#     print("End index:", match.end())

#Find all occurrence of a pattern
# matches = re.findall("the", text, re.IGNORECASE) #Case-insenitive search
# print("Matches:", matches)

new_text = re.sub("fox","cat", text)
print("New text:", new_text)



