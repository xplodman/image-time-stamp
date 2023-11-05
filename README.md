# Image time stamp

Image time stamp is a Python project that allows you to add date and time stamps to your images. It extracts the date and time from the EXIF metadata of your photos and embeds it in the image, providing a quick and easy way to preserve and display the moment a photo was taken.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatically extracts the date and time from the EXIF metadata of photos.
- Adds a customizable timestamp to the bottom right corner of the image.
- Supports common image formats, including JPEG, PNG, and GIF.
- Simple and easy-to-use Python script.

## Installation

1. Clone or download the repository:

```bash
git clone https://github.com/yourusername/ImageTimeStamp.git
```

2. Install the required Python libraries:

```bash
pip install pillow
```

## Usage

1. Place your images in the project folder.

2. Run the script to add timestamps to your images. The timestamp will be added to the bottom right corner of each image.

```bash
python add_timestamp.py
```

3. The modified images will be saved with the prefix "timestamp_" in the same folder.

4. You can customize the font, font size, and text color in the `add_timestamp.py` script to suit your preferences.

## Contributing

If you'd like to contribute to this project, feel free to open issues or pull requests. We welcome any suggestions, bug reports, or feature requests.

- Fork the repository.
- Create your feature branch: `git checkout -b feature-name`
- Commit your changes: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature-name`
- Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---