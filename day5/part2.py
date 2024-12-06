def read_rules(rules_file: str):
    with open(rules_file) as file:
        return [([line.strip().split("|")[0], line.strip().split("|")[1]]) for line in file]

def read_updates(updates_file: str):
    with open(updates_file) as file:
        return [line.strip().split(",") for line in file]

class Page:
    rules = read_rules("rules_a.txt")

    def __init__(self, page: str):
        self.page = page

    def __gt__(self, other):
        if [self.page, other.page] in Page.rules:
            return True

    def get_page(self):
        return self.page
    
    def __str__(self):
        return self.page
        
def check_rules(update):
    pages = [Page(i) for i in update]
    return all(pages[i] > pages[i + 1] for i in range(len(pages) - 1))
    

def get_sorted(update):
    pages = [Page(page) for page in update]
    return sorted(pages, reverse=True)

def main():
    updates = read_updates("updates_a.txt")
    total = 0
    for update in updates:
        if not check_rules(update):
            sorted = get_sorted(update)
            total += int(sorted[len(sorted) // 2].get_page())
    print(total)

if __name__ == "__main__":
    main()