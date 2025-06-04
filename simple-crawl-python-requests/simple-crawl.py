import requests
from bs4 import BeautifulSoup

# Bước 1: Gửi request
url = "https://example.com"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# Bước 2: Phân tích HTML
soup = BeautifulSoup(response.text, "html.parser")

# Bước 3: Trích xuất dữ liệu (ví dụ: tiêu đề trong <h1>)
# title = soup.find("h1")
# paragraph = soup.find("p")
# print("Tiêu đề trang:", title.text.strip() if title else "Không tìm thấy")
# print("Đoạn văn:", paragraph.text.strip() if paragraph else "Không tìm thấy")

# Tìm tất cả
all_paragraphs = soup.find_all("p")
# for p in all_paragraphs:
#     print(p.text.strip())
#     print("--------------------------------")

p_with_a = all_paragraphs[-1]

print('--p_with_a', p_with_a)

a_tag = p_with_a.find("a")

print('--a_tag', a_tag)

print('--a_tag.text', a_tag.text)

print('--a_tag.get("href")', a_tag.get("href"))



