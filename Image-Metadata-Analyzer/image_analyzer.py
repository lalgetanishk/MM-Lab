import os
from PIL import Image, ExifTags

SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".bmp"}

def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes / (1024 * 1024):.2f} MB"

def analyze_image(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError("Image file does not exist.")

    ext = os.path.splitext(image_path)[1].lower()
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported image format: {ext}")

    with Image.open(image_path) as img:
        width, height = img.size
        dpi = img.info.get("dpi")
        exif = img.getexif()

        lines = [
            "=" * 40,
            "IMAGE METADATA REPORT",
            "=" * 40,
            f"File Name       : {os.path.basename(image_path)}",
            f"File Size       : {format_size(os.path.getsize(image_path))}",
            f"File Format     : {img.format}",
            f"Width           : {width} pixels",
            f"Height          : {height} pixels",
            f"Resolution      : {dpi if dpi else 'Not Available'}",
            f"Color Mode      : {img.mode}",
            "",
            "EXIF Metadata",
            "-" * 40,
        ]

        if exif:
            for tag_id, value in exif.items():
                tag = ExifTags.TAGS.get(tag_id, str(tag_id))
                lines.append(f"{tag:<20}: {value}")
        else:
            lines.append("No EXIF metadata found.")

    report = "\n".join(lines)
    print(report)

    with open("image_output.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("\nReport saved as image_output.txt")

if __name__ == "__main__":
    path = input("Enter image path: ").strip().strip('"')
    try:
        analyze_image(path)
    except Exception as e:
        print("Error:", e)
