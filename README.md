# Quran Images Utils

[![License Badge](https://img.shields.io/github/license/QuranHub/quran-images-utils)](https://github.com/QuranHub/quran-images-utils/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

![QuranHub Banner Image](https://www.quranhub.app/image/quranhub_banner.png)

Utility scripts for Quran images.

## How to use the scripts?

1. Use `image_downloader/download_pages.py` to download Quran pages images from sources like [KFGQPC website][1]: [Hafs][2] or [other recitations][3].
2. Use `image_prepare/prepare_imgs.py` to process & prepare of the original Quran pages images for example crop, resize, optimize, etc.
3. Use `aya_locator/aya_locator.py` to detect the ayas locations in the Quran pages images and generate a CSV file of those data.
4. Finally, you can use `csv_to_sqlite_db/csv_to_sqlite.py` to convert the CSV data to a SQLite DB.

[1]: https://qurancomplex.gov.sa/
[2]: https://qurancomplex.gov.sa/kfgqpc-quran-hafs/
[3]: https://qurancomplex.gov.sa/kfgqpc-quran-qiraat/

## Contributing
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please read [CONTRIBUTING.md](https://github.com/QuranHub/quran-images-utils/blob/master/CONTRIBUTING.md) for our code of conduct and details on contributing to the project.

#### Steps for contributing to this repository:
1.  Fork it.
2.  Create your feature branch:  `git checkout -b my-new-feature`
3.  Commit your changes:  `git add .`  `git commit -m 'Add some feature'`
4.  Push to the branch:  `git push origin my-new-feature`
5.  Create new Pull Request.

## License

This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/QuranHub/quran-images-utils/blob/master/LICENSE) file for details.
