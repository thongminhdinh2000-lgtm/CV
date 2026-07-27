# ==========================================
# step5_report.py
# Thống kê & Log lỗi
# ==========================================

import time
import pandas as pd

from config import (
    REPORT_FILE,
    LOG_FILE,
    OUTPUT_EXCEL
)


def create_report(
        xml_files,
        success_files,
        error_files,
        data,
        start_time
):

    print("\n" + "=" * 60)
    print("BƯỚC 5 - THỐNG KÊ")
    print("=" * 60)

    # =====================================
    # Thống kê
    # =====================================

    total_file = len(xml_files)

    success = len(set(success_files))

    failed = len(error_files)

    total_row = len(data)

    invoice_count = len(
        set(
            row["Số HĐ"]
            for row in data
            if row.get("Số HĐ")
        )
    )

    elapsed = round(
        time.time() - start_time,
        2
    )

    # =====================================
    # Xuất ThongKe.xlsx
    # =====================================

    report = pd.DataFrame({

        "Chỉ tiêu": [

            "Tổng số file XML",

            "File thành công",

            "File lỗi",

            "Tổng số hóa đơn",

            "Tổng số dòng hàng",

            "Thời gian chạy (giây)",

            "File Excel"

        ],

        "Giá trị": [

            total_file,

            success,

            failed,

            invoice_count,

            total_row,

            elapsed,

            OUTPUT_EXCEL

        ]

    })

    report.to_excel(
        REPORT_FILE,
        index=False
    )

    # =====================================
    # Xuất Log lỗi
    # =====================================

    if len(error_files):

        log = pd.DataFrame(error_files)

        log.to_excel(
            LOG_FILE,
            index=False
        )

    # =====================================
    # In màn hình
    # =====================================

    print(f"Tổng số file XML      : {total_file:,}")
    print(f"File thành công       : {success:,}")
    print(f"File lỗi              : {failed:,}")
    print(f"Tổng số hóa đơn       : {invoice_count:,}")
    print(f"Tổng số dòng hàng     : {total_row:,}")
    print(f"Thời gian chạy        : {elapsed:,} giây")

    print("\nĐã xuất:")

    print(f"Excel     : {OUTPUT_EXCEL}")

    print(f"Thống kê  : {REPORT_FILE}")

    if failed:
        print(f"Log lỗi   : {LOG_FILE}")

    print("=" * 60)  
