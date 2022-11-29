pages = input()
teared_page = input()
remaining_pages = input()

result = 0

for page in range(1,int(pages) + 1):
    if str(page) not in remaining_pages.split():
        if teared_page in str(page):
            if int(page) == int(pages):
                result += 1
            elif int(page) != int(pages):
                if teared_page in str(page + 1) and (int(page) + 1) >= 20:
                    result += 1
                else:
                    result += 2

print(result)