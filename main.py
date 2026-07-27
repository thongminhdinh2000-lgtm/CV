# ==========================================
# main.py
# Chương trình chính
# ==========================================

import time

from step1_scan import scan_xml
from step2_read_xml import read_all_xml
from step3_export import export_excel
from step4_move import move_processed
from step5_report import create_report


def main():

    # ==============================
    # Bắt đầu tính thời gian
    # ==============================

    start_time = time.time()

    print("\n")
    print("=" * 70)
    print("CHƯƠNG TRÌNH CHUYỂN XML HÓA ĐƠN -> EXCEL")
    print("=" * 70)

    # ==============================
    # BƯỚC 1
    # ==============================

    xml_files = scan_xml()

    if len(xml_files) == 0:

        print("\nKhông tìm thấy file XML.")

        return

    # ==============================
    # BƯỚC 2
    # ==============================

    data, success_files, error_files = read_all_xml(
        xml_files
    )

    # ==============================
    # BƯỚC 3
    # ==============================

    output_file = export_excel(data)

    # ==============================
    # BƯỚC 4
    # ==============================

    moved_files, move_errors = move_processed(
        success_files
    )

    # Gộp lỗi chuyển file vào log lỗi

    if len(move_errors):

        error_files.extend(move_errors)

    # ==============================
    # BƯỚC 5
    # ==============================

    create_report(

        xml_files=xml_files,

        success_files=success_files,

        error_files=error_files,

        data=data,

        start_time=start_time

    )

    print("\nHoàn thành.")


if __name__ == "__main__":

    main()
