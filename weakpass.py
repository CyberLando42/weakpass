import hashlib
import random
random_num = random.randrange(1, 14000000)
i = 0
print("Finding password from rockyou.txt...")
f = open("/usr/share/wordlists/rockyou.txt", encoding="utf-8", errors="ignore")
for line in f:
	
	line2 = line.strip()
	if i == random_num:
		print(f"Yay! You now have an insecure password: {line2}")
	i += 1
f.close()
