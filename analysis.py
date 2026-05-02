import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-pro")

def analyze_market(news_text):
    prompt = f"""
Bạn là một Macro Liquidity Analyst chuyên phân tích thị trường tài chính Việt Nam theo framework "bồn tín dụng".

NHIỆM VỤ:
Phân tích dữ liệu tin tức thị trường tiền tệ và tạo báo cáo theo logic dòng tiền chuyên nghiệp (giống analyst quỹ đầu tư, không phải tin tức).

=====================
INPUT (TIN TỨC):
{news_text}
=====================

YÊU CẦU PHÂN TÍCH (BẮT BUỘC THEO THỨ TỰ):

Bước 1 — Trích xuất dữ liệu:
- Lãi suất liên ngân hàng O/N (%)
- Xu hướng lãi suất
- OMO bơm/hút (tỷ)
- Quy mô

Bước 2 — Pattern:
- Lãi suất phản ứng thế nào với OMO?

Bước 3 — Dòng tiền:
- Thiếu tiền / siết tiền / nhiễu

Bước 4 — Trạng thái:
- Thanh khoản: dư / căng / kiểm soát

Bước 5 — CASE:
- Chọn CASE (1–7) + giải thích

Bước 6 — Hành động:
- PRE-BUY / PRE-SELL / NEUTRAL
- Strategy cụ thể

=====================
FORMAT OUTPUT:

📊 Weekly Liquidity Report

1. Diễn biến dữ liệu
...

2. Pattern thị trường
...

3. Phân tích dòng tiền
...

4. Trạng thái hệ thống
...

5. CASE:
...

6. Hành động:
...

7. Tóm tắt 1 dòng:
...

=====================

QUY TẮC:
- Viết như macro analyst (quỹ đầu tư)
- Có reasoning (cause → effect)
- Không viết kiểu báo chí
"""

    response = model.generate_content(prompt)
    return response.text