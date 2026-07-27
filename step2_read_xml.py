# ==========================================
# step2_read_xml.py
# Đọc dữ liệu XML
# ==========================================

import zipfile
import xml.etree.ElementTree as ET


# ==========================================
# Hàm lấy text
# ==========================================

def get_text(parent, tag):

    if parent is None:
        return ""

    node = parent.find(tag)

    if node is None:
        return ""

    return (node.text or "").strip()


# ==========================================
# Đọc 1 XML
# ==========================================

def read_one_xml(root, file_name):

    rows = []

    dl = root.find("DLHDon")

    if dl is None:
        raise Exception("Không tìm thấy DLHDon")

    tt = dl.find("TTChung")
    nd = dl.find("NDHDon")

    nban = nd.find("NBan")
    nmua = nd.find("NMua")
    dshh = nd.find("DSHHDVu")
    ttoan = nd.find("TToan")

    # Thông tin hóa đơn

    invoice = {

        "Tên file": file_name,
        "Số HĐ": get_text(tt, "SHDon"),
        "Mẫu số": get_text(tt, "KHMSHDon"),
        "Ký hiệu": get_text(tt, "KHHDon"),
        "Ngày lập": get_text(tt, "NLap"),

        "Tên người bán": get_text(nban, "Ten"),
        "MST người bán": get_text(nban, "MST"),
        "Địa chỉ người bán": get_text(nban, "DChi"),

        "Tên người mua": get_text(nmua, "Ten"),
        "MST người mua": get_text(nmua, "MST"),
        "Địa chỉ người mua": get_text(nmua, "DChi"),

        "Hình thức thanh toán": get_text(tt, "HTTToan"),

        "Tổng tiền trước thuế": get_text(ttoan, "TgTCThue"),
        "Tổng tiền thuế": get_text(ttoan, "TgTThue"),
        "Tổng thanh toán": get_text(ttoan, "TgTTTBSo")

    }

    # Nếu không có hàng hóa

    if dshh is None:

        rows.append(invoice)

        return rows

    # Đọc từng mặt hàng

    for hh in dshh.findall("HHDVu"):

        row = invoice.copy()

        row["STT"] = get_text(hh, "STT")
        row["Mã hàng"] = get_text(hh, "MHHDVu")
        row["Tên hàng"] = get_text(hh, "THHDVu")
        row["ĐVT"] = get_text(hh, "DVTinh")
        row["Số lượng"] = get_text(hh, "SLuong")
        row["Đơn giá"] = get_text(hh, "DGia")
        row["Chiết khấu"] = get_text(hh, "STCKhau")
        row["Thành tiền"] = get_text(hh, "ThTien")
        row["Thuế suất"] = get_text(hh, "TSuat")
        row["Tiền thuế"] = get_text(hh, "TThue")

        rows.append(row)

    return rows


# ==========================================
# Đọc toàn bộ XML
# ==========================================

def read_all_xml(xml_list):

    data = []

    success_files = []

    error_files = []

    total = len(xml_list)

    print("\n" + "=" * 60)
    print("BƯỚC 2 - ĐỌC XML")
    print("=" * 60)

    for i, item in enumerate(xml_list, start=1):

        try:

            # ===============================
            # XML thường
            # ===============================

            if item["type"] == "xml":

                tree = ET.parse(item["path"])

                root = tree.getroot()

                rows = read_one_xml(
                    root,
                    item["path"]
                )

                data.extend(rows)

                success_files.append(item["path"])

                print(f"[{i}/{total}] OK : {item['path']}")

            # ===============================
            # XML trong ZIP
            # ===============================

            else:

                with zipfile.ZipFile(item["zip_path"]) as z:

                    with z.open(item["xml_name"]) as f:

                        tree = ET.parse(f)

                        root = tree.getroot()

                        rows = read_one_xml(
                            root,
                            item["xml_name"]
                        )

                        data.extend(rows)

                success_files.append(item["zip_path"])

                print(
                    f"[{i}/{total}] OK : "
                    f"{item['zip_path']} -> {item['xml_name']}"
                )

        except Exception as e:

            if item["type"] == "xml":

                file_error = item["path"]

            else:

                file_error = (
                    item["zip_path"]
                    + " -> "
                    + item["xml_name"]
                )

            error_files.append({

                "File": file_error,

                "Lỗi": str(e)

            })

            print(f"[{i}/{total}] LỖI : {file_error}")

    print("=" * 60)

    print(f"Tổng dòng dữ liệu : {len(data):,}")

    print(f"Thành công        : {len(success_files):,}")

    print(f"Lỗi               : {len(error_files):,}")

    print("=" * 60)

    return data, success_files, error_files
