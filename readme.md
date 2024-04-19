# CR3 Viewer

CR3 Viewer is a Python application built using Tkinter and PIL, designed to view and save Canon Raw version 3 (CR3) files. It provides a simple GUI to open, display, and save CR3 files as JPEG or PNG images.

## Features

- **Open CR3 Files**: Browse and select one or multiple CR3 files to view.
- **Display Images**: Thumbnails of the selected CR3 files are displayed in tabs for easy navigation.
- **Save Images**: Save the currently viewed CR3 file as a JPEG or PNG image.

## Requirements

To run CR3 Viewer, you need Python installed on your system along with the following packages:
- Tkinter (usually comes with Python)
- PIL (Pillow)
- rawpy
- imageio
- tkinterdnd2

## Installation

1. Ensure you have Python installed on your system.
2. Install the required Python packages using pip:

pip install Pillow rawpy imageio tkinterdnd2

## Usage

To start the application, run the script with Python:

python main.py

Once the application is running:
- Click on the **New** button to open and select CR3 files.
- The selected files will be opened in new tabs within the application window.
- Click on a tab to view the image.
- Click on the **Save** button to save the currently displayed image as a JPEG or PNG file.

## Contributing

Contributions to CR3 Viewer are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

CR3 Viewer is released under the MIT License. See the LICENSE file for more details.
