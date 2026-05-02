import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_market(news_text):
    prompt = f"""
    Bạn là chuyên gia phân tích thị trường tài chính Việt Nam.

    Dựa trên framework:
    - Lãi suất liên ngân hàng
    - OMO (bơm/hút tiền)
    - Tín dụng
    - Margin

    Hãy đọc tin sau:

    {news_text}

    Thực hiện:
    1. Trích xuất dữ liệu:
       - Lãi suất O/N (%)
       - OMO bơm/hút (tỷ)
    2. Xác định trạng thái thị trường:
       - Thanh khoản căng / dư
    3. Phân loại:
       - PRE-BUY / PRE-SELL / NEUTRAL
    4. Viết báo cáo ngắn gọn

    Trả về format:

    📊 Weekly Liquidity Report

    Data:
    - Interbank:
    - OMO:

    Nhận định:
    ...

    Hành động:
    ...
    """

    response = model.generate_content(prompt)
    return response.text