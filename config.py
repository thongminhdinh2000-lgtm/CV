# ==========================================
# config.py
# Cấu hình chương trình
# ==========================================

import os
from datetime import datetime

# ==========================================
# THƯ MỤC
# ==========================================

# Thư mục chứa XML cần xử lý
INPUT_FOLDER = r"D:\Hoadon\Downloads"

# Thư mục xuất Excel
OUTPUT_FOLDER = r"D:\Hoadon\Output"

# Thư mục lưu XML đã xử lý
PROCESSED_FOLDER = r"D:\Hoadon\Processed"

# ==========================================
# TÊN FILE OUTPUT
# ==========================================

CURRENT_TIME = datetime.now().strftime("%Y%m%d_%H%M%S")

OUTPUT_EXCEL = os.path.join(
    OUTPUT_FOLDER,
    f"HoaDon_{CURRENT_TIME}.xlsx"
)

LOG_FILE = os.path.join(
    OUTPUT_FOLDER,
    "Log_Loi.xlsx"
)

REPORT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "ThongKe.xlsx"
)

# ==========================================
# TỰ TẠO THƯ MỤC NẾU CHƯA CÓ
# ==========================================

for folder in [
    INPUT_FOLDER,
    OUTPUT_FOLDER,
    PROCESSED_FOLDER
]:
    os.makedirs(folder, exist_ok=True)

# ==========================================
# CÁC CỘT XUẤT EXCEL
# ==========================================

EXCEL_COLUMNS = [
    "Tên file",
    "Số HĐ",
    "Mẫu số",
    "Ký hiệu",
    "Ngày lập",

    "Tên người bán",
    "MST người bán",
    "Địa chỉ người bán",

    "Tên người mua",
    "MST người mua",
    "Địa chỉ người mua",

    "Hình thức thanh toán",

    "STT",
    "Mã hàng",
    "Tên hàng",
    "ĐVT",
    "Số lượng",
    "Đơn giá",
    "Chiết khấu",
    "Thành tiền",
    "Thuế suất",
    "Tiền thuế",

    "Tổng tiền trước thuế",
    "Tổng tiền thuế",
    "Tổng thanh toán"
]

# ==========================================
# HIỂN THỊ THÔNG TIN
# ==========================================

if __name__ == "__main__":

    print("=" * 60)
    print("CẤU HÌNH CHƯƠNG TRÌNH")
    print("=" * 60)

    print("INPUT      :", INPUT_FOLDER)
    print("OUTPUT     :", OUTPUT_FOLDER)
    print("PROCESSED  :", PROCESSED_FOLDER)

    print("\nFile Excel :", OUTPUT_EXCEL)
    print("Log lỗi    :", LOG_FILE)
    print("Thống kê   :", REPORT_FILE)

    print("=" * 60)
