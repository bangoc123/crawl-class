from bs4 import BeautifulSoup
html_string = """
<html>
  <head><title>Trang demo</title></head>
  <body>
    <h1>Xin chào!</h1>
    <p class="desc">Đây là đoạn mô tả</p>
    <p class="desc">Đây là đoạn mô tả 2</p>
    <p class="outer-desc">
        <p class="inner-desc-1">Đây là đoạn mô tả bên trong</p>
        <p class="inner-desc-2">Đây là đoạn mô tả bên trong 2</p>
        <p class="target">Đây là đoạn mô tả bên trong 3</p>
        <a href="https://blog.example.com">Trang phụ</a>
        <p class="target-2">Đây là đoạn mô tả bên trong 3</p>
    </p>
    <a href="https://example.com">Trang chính</a>
    <h1>Bye bye</h1>
  </body>
</html>
"""

soup = BeautifulSoup(html_string, "html.parser")

target_p = soup.find("p", class_="target")

# Find siblings of target_p

sibling = target_p.find_next_sibling()

print(sibling)
