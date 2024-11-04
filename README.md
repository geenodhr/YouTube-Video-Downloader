# 📥✨ YouTube Video Downloader ✨📥  
<p align="center">
    <img src="/main/yt-downloader-logo.ico" alt="YouTube Video Downloader Icon" width="100" height="100"/>
</p>

A standalone desktop application to easily download YouTube videos in MP4 format with great audio quality. Just paste the URL, select your desired resolution, and enjoy your video offline in seconds!

---

## 📜 Description

YouTube Video Downloader is a simple, user-friendly tool designed to download YouTube videos with ease. Whether you want to save your favorite content for offline access, watch videos without ads, or simply keep a local copy of content, this application offers an intuitive way to make that happen. Built with Python, it provides a smooth experience by integrating a thumbnail preview, resolution selection, and download progress tracking—all in a sleek GUI.

---

## 🚀 How It Works

Using this tool is quick and straightforward! Here’s how you can download your favorite YouTube videos:

1. **Paste the URL**: Enter the YouTube video URL into the provided field.
2. **Preview the Video**: The thumbnail and title of the video will display below the URL field, helping you confirm the video.
3. **Choose Resolution**: From the dropdown, select your preferred video quality.
4. **Select Destination**: Pick the folder where you’d like to save the downloaded video.
5. **Start Download**: Click the “Download” button, and watch the progress bar as it indicates the download status.

The video is downloaded in MP4 format with excellent audio quality, ready for offline enjoyment!

---

## ⚙️ Features

- **Intuitive GUI**: Simple, user-friendly interface.
- **Preview Video**: Display of video thumbnail and title.
- **Quality Selection**: Choose from available resolutions.
- **MP4 Format**: Downloads are saved in MP4 with high audio fidelity.
- **Download Progress**: Progress bar updates with download status.

---

## 🖥️ Running the Application

You can run this application in two ways:

### Option 1: Using the Pre-Built Executable
1. Download the executable file: **`YT Video Downloader.exe`** from the `dist` folder or the [Releases](https://github.com/username/repository/releases) section on GitHub.
2. Run `YT Video Downloader.exe` by double-clicking it.
3. Follow the on-screen instructions to download videos as described above.

### Option 2: Building from Source with PyInstaller
If you prefer, you can generate your own `dist` and `build` folders by building the executable with `pyinstaller`.

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
2. **Build the Executable**:
   Run the following command in the root folder of the project:
   ```bash
   pyinstaller --onefile --windowed yt-downloader.py
   ```
   This will create a `dist` folder with the executable file inside.

3. **Run the Application**:
   - Navigate to the `dist` folder, where you’ll find the generated executable (`YT Video Downloader.exe`).
   - Run the application by double-clicking the executable.

---

## 🌐 Future Plans

- Expanded resolution options
- Support for downloading only audio
- Enhanced error handling and user feedback

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy hassle-free YouTube downloading with this easy-to-use tool!
