# ==========================================
# step1_scan.py
# Quét toàn bộ file XML trong thư mục Downloads
# ==========================================

import os
from config import INPUT_FOLDER


def scan_xml():
    """
    Quét tất cả file XML trong INPUT_FOLDER
    (bao gồm cả thư mục con)

    Returns
    -------
    list
        Danh sách đường dẫn đầy đủ của file XML
    """

    xml_files = []

    print("\n" + "=" * 60)
    print("BƯỚC 1: QUÉT FILE XML")
    print("=" * 60)

    # Kiểm tra thư mục tồn tại
    if not os.path.exists(INPUT_FOLDER):
        raise FileNotFoundError(
            f"Không tìm thấy thư mục:\n{INPUT_FOLDER}"
        )

    # Quét thư mục
    for root, dirs, files in os.walk(INPUT_FOLDER):

        for file in files:

            # Chỉ lấy XML
            if file.lower().endswith(".xml"):

                full_path = os.path.join(root, file)

                xml_files.append(full_path)

    # Sắp xếp theo tên
    xml_files.sort()

    print(f"Tổng số file XML tìm thấy : {len(xml_files):,}")

    if len(xml_files) == 0:
        print("Không tìm thấy file XML.")
    else:

        print("\nDanh sách 10 file đầu tiên:")

        for i, file in enumerate(xml_files[:10], start=1):
            print(f"{i:>3}. {os.path.basename(file)}")

        if len(xml_files) > 10:
            print("...")

    print("=" * 60)

    return xml_files


# =====================================================
# Chạy riêng để kiểm tra
# =====================================================

if __name__ == "__main__":

    xml_files = scan_xml()

    print("\nKiểm tra thành công.")
    print(f"Tổng số file XML: {len(xml_files):,}")
