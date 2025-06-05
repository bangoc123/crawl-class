from bs4 import BeautifulSoup
html_string = """
<html>
  <head><title>Trang demo</title></head>
  <body>
    <h1>Xin chào!</h1>
    <p class="desc">Đây là đoạn mô tả</p>
    <p class="desc">Đây là đoạn mô tả 2</p>
    <p class="outer-desc">
        <p class="inner-desc">Đây là đoạn mô tả bên trong</p>
        <p class="inner-desc">Đây là đoạn mô tả bên trong 2</p>
        <p class="inner-desc">Đây là đoạn mô tả bên trong 3</p>
    </p>
    <a href="https://example.com">Trang chính</a>
    <h1>Bye bye</h1>
  </body>
</html>
"""

soup = BeautifulSoup(html_string, "html.parser")

# print(soup.prettify())

# print(soup.title)

# Find all elements

h1s = soup.find_all("h1")

for h1 in h1s:
    print(h1.text)

# Find the first element

first_h1 = soup.find("h1")

print(first_h1.text)

# Find all elements with class "desc"
print('--------------------------------')
descs = soup.find_all("p", class_="desc")

for desc in descs:
    print(desc.text)

print('--------------Find p inside p------------------')
# Find all elements with class "outer-desc"
inner_desc = soup.find("p", class_="outer-desc").find("p", class_="inner-desc")

print(inner_desc.text)

# Use soup.select to find elements

print('--------------Use soup.select to find elements------------------')

descs = soup.select("p.outer-desc > p.inner-desc")

for desc in descs:
    print(desc.text)








