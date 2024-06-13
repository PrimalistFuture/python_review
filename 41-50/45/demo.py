from bs4 import BeautifulSoup

with open("41-50/45/bs4-start/website.html", "r", encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.name)
print(soup.prettify())
print(soup.p)  # only gives the first p tag
print(soup.find_all(name="p"))  # now finds all p tags

all_a_tags = soup.find_all(name="a")  # now finds all a tags

for tag in all_a_tags:
    print(tag.getText())  # just prints the text of the tag
    print(tag.get("href"))  # prints value of the href attribute


# still only gets the first, but has to meet both criteria (name and id)
heading = soup.find(name="h1", id="name")

# notice the _ to search for a class and not create a class
section_heading = soup.find(name="h3", class_="heading")

# using CSS selectors to find what we want = an a tag nested in a p tag
company_url = soup.select_one(selector="p a")

# using CSS to select element by an id
name = soup.select_one(selector="#name")

# using CSS to select all elements with the class of heading
soup.select(selector=".heading")
