text = input().lower()

counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1

top_three = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:3]

for char, count in top_three:
    print(f"{char}: {count}")
