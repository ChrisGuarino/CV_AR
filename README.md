# CV_AR: OpenCV Augmented Reality

Real-time augmented reality using OpenCV, supporting ArUco marker detection and ORB feature matching to overlay images, videos, and 3D models onto a camera feed.

## Features

- **3D Model Projection** — Detect a reference surface via ORB feature matching and render OBJ models onto it with perspective correction
- **Image Overlay** — Warp and blend a source image onto ArUco marker corners
- **Video Overlay** — Stream video onto detected markers with frame buffering and marker caching for occlusion handling
- **OBJ Loader** — Parse Wavefront OBJ files (vertices, normals, texture coordinates, faces)

## Scripts

| Script | Description |
|--------|-------------|
| `AR_3D.py` | ORB-based surface detection with 3D OBJ model rendering |
| `opencv_ar_image.py` | ArUco marker detection with image overlay |
| `opencv_ar_video.py` | ArUco marker detection with video overlay |
| `augmented_reality.py` | Core AR utilities |
| `objloader_simple.py` | Wavefront OBJ file parser |

## Requirements

- Python 3
- OpenCV (with ArUco contrib module)
- NumPy
- imutils

## Usage

```bash
# 3D model overlay using ORB feature matching
python AR_3D.py

# Image overlay using ArUco markers
python opencv_ar_image.py

# Video overlay using ArUco markers
python opencv_ar_video.py
```

## Project Structure

```
CV_AR/
├── AR_3D.py                # 3D model projection via ORB matching
├── augmented_reality.py    # Core AR functions
├── opencv_ar_image.py      # ArUco marker image overlay
├── opencv_ar_video.py      # ArUco marker video overlay
├── objloader_simple.py     # OBJ file parser
├── CV_ARUCO/               # ArUco marker assets
├── 3D/                     # 3D model files (OBJ)
├── image/                  # Reference images
├── source/                 # Source overlay content
└── video/                  # Video overlay content
```
