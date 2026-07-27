# ==========================================
# step4_move.py
# Chuyển file đã xử lý
# ==========================================

import os
import shutil

from config import PROCESSED_FOLDER


# ==========================================
# Sinh tên mới nếu bị trùng
# ==========================================

def get_new_filename(dest_path):

    if not os.path.exists(dest_path):
        return dest_path

    folder = os.path.dirname(dest_path)

    filename = os.path.basename(dest_path)

    name, ext = os.path.splitext(filename)

    index = 1

    while True:

        new_name = f"{name}_{index}{ext}"

        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            return new_path

        index += 1


# ==========================================
# Chuyển file
# ==========================================

def move_processed(success_files):

    print("\n" + "=" * 60)
    print("BƯỚC 4 - CHUYỂN FILE")
    print("=" * 60)

    moved = 0
    failed = 0

    moved_files = []
    failed_files = []

    # Loại bỏ file trùng
    unique_files = []

    for file in success_files:

        if file not in unique_files:
            unique_files.append(file)

    total = len(unique_files)

    for i, source in enumerate(unique_files, start=1):

        try:

            filename = os.path.basename(source)

            destination = os.path.join(
                PROCESSED_FOLDER,
                filename
            )

            destination = get_new_filename(destination)

            shutil.move(
                source,
                destination
            )

            moved += 1

            moved_files.append(destination)

            print(f"[{i}/{total}] OK : {filename}")

        except Exception as e:

            failed += 1

            failed_files.append({
                "File": source,
                "Lỗi": str(e)
            })

            print(f"[{i}/{total}] LỖI : {source}")

    print("=" * 60)

    print(f"Đã chuyển : {moved:,}")

    print(f"Lỗi       : {failed:,}")

    print("=" * 60)

    return moved_files, failed_files
