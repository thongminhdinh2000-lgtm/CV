# ==========================================
# step1_scan.py
# Quét XML và XML trong ZIP
# ==========================================

import os
import zipfile
from config import INPUT_FOLDER


def scan_xml():

    xml_list = []

    total_xml = 0
    total_zip = 0

    print("=" * 60)
    print("BƯỚC 1 - QUÉT XML")
    print("=" * 60)

    if not os.path.exists(INPUT_FOLDER):
        raise FileNotFoundError(INPUT_FOLDER)

    for root, dirs, files in os.walk(INPUT_FOLDER):

        for file in files:

            full_path = os.path.join(root, file)

            # =================================================
            # XML bình thường
            # =================================================
            if file.lower().endswith(".xml"):

                xml_list.append({
                    "type": "xml",
                    "path": full_path
                })

                total_xml += 1

            # =================================================
            # ZIP
            # =================================================
            elif file.lower().endswith(".zip"):

                total_zip += 1

                try:

                    with zipfile.ZipFile(full_path, "r") as z:

                        for member in z.namelist():

                            if member.lower().endswith(".xml"):

                                xml_list.append({

                                    "type": "zip",

                                    "zip_path": full_path,

                                    "xml_name": member

                                })

                except Exception as e:

                    print(f"Lỗi đọc ZIP: {file}")
                    print(e)

    print(f"Tìm thấy {total_xml:,} file XML.")
    print(f"Tìm thấy {total_zip:,} file ZIP.")
    print(f"Tổng XML sẽ xử lý: {len(xml_list):,}")

    print("\n10 file đầu tiên:\n")

    for i, item in enumerate(xml_list[:10], start=1):

        if item["type"] == "xml":

            print(f"{i}. XML  : {os.path.basename(item['path'])}")

        else:

            print(
                f"{i}. ZIP  : "
                f"{os.path.basename(item['zip_path'])}"
                f" -> {item['xml_name']}"
            )

    print("=" * 60)

    return xml_list


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    xml_files = scan_xml()

    print()

    print(f"Tổng XML cần đọc: {len(xml_files):,}")
