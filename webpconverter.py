#!/usr/bin/env python3

import cv2
import os
from pathlib import Path
import argparse

def convert_to_webp(folder_path,replace=False):
    folder = Path(folder_path)
    if not folder.exists():
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    for file_path in folder.rglob("*"):
        if file_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            webp_path = file_path.with_suffix(".webp")
            
            if webp_path.exists():
                print(f"Skipping {file_path} as {webp_path} already exists.")
                continue

            try:
                jpg_img = cv2.imread(file_path)
                # Resize image to 50% of the original size
                resized_image = cv2.resize(jpg_img, (int(jpg_img.shape[1] * 0.5), int(jpg_img.shape[0] * 0.5)))
                cv2.imwrite(webp_path, resized_image, [int(cv2.IMWRITE_WEBP_QUALITY), 50])

                if replace:
                    os.remove(file_path)

                print(f"Converted {file_path} to {webp_path}")

            except Exception as e:
                print(f"Failed to convert {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert images to WEBP format.")
    parser.add_argument(
        "folder",
        type=str,
        help="Path to the folder containing images to convert",
    )

    parser.add_argument(
        "-r", "--replace",
        action="store_true",
        help="Replace existing WEBP files and delete original images",
    )

    args = parser.parse_args()
    convert_to_webp(args.folder, replace=args.replace)

if __name__ == "__main__":
    main()
