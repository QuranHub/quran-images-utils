# Quran Images Utils

Utility scripts for Quran images.

## How to use the scripts?

1. Use `image_downloader/download_pages.py` to download Quran pages images from sources like [KFGQPC website][1]: [Hafs][2] or [other recitations][3].
2. Use `image_prepare/prepare_imgs.py` to process & prepare of the original Quran pages images for example crop, resize, optimize, etc.
3. Use `aya_locator/aya_locator.py` to detect the ayas locations in the Quran pages images and generate a CSV file of those data.
4. Finally, you can use `csv_to_sqlite_db/csv_to_sqlite.py` to convert the CSV data to a SQLite DB.

[1]: https://qurancomplex.gov.sa/
[2]: https://qurancomplex.gov.sa/kfgqpc-quran-hafs/
[3]: https://qurancomplex.gov.sa/kfgqpc-quran-qiraat/