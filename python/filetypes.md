从依赖包分析，应该可处理

- .avi
- .bat
- .blp
- .bmp
- .bz2
- .csv
- .db
- .dds
- .dib
- .docx
- .eps
- .epub
- .FLAC
- .flv
- .gif
- .gz
- .html
- .HTK
- .icns
- .ico
- .im
- .ini
- .IRCAM
- .jpeg
- .jpg
- .json
- .log
- .MAT4
- .MAT5
- .md
- .mov
- .mobi
- .mp3
- .mp4
- .MPC2K
- .msp
- .NIST
- .ogg
- .PAF
- .pcx
- .pdf
- .png
- .ppm
- .ppt (PowerPoint)
- .pptx (PowerPoint)
- .PVF
- .py
- .RAW
- .RF64
- .rtf
- .SD2
- .SDS
- .sh
- .sqlite
- .svg
- .SVX
- .tar
- .tga
- .tiff
- .txt
- .VOC
- .W64
- .wav
- .WAVEX
- .webp
- .wmv
- .WVE
- .xls (Excel)
- .xlsm (Excel)
- .xlsx (Excel)
- .xbm
- .XI
- .xml
- .xz
- .yml (YAML)
- .zip

## ref

- Ignore read only formats of pillow, Fully supported formats from https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
- soundfile:
  - ```
    sf.available_formats()
    Out[3]: 
    {'AIFF': 'AIFF (Apple/SGI)',
     'AU': 'AU (Sun/NeXT)',
     'AVR': 'AVR (Audio Visual Research)',
     'CAF': 'CAF (Apple Core Audio File)',
     'FLAC': 'FLAC (Free Lossless Audio Codec)',
     'HTK': 'HTK (HMM Tool Kit)',
     'SVX': 'IFF (Amiga IFF/SVX8/SV16)',
     'MAT4': 'MAT4 (GNU Octave 2.0 / Matlab 4.2)',
     'MAT5': 'MAT5 (GNU Octave 2.1 / Matlab 5.0)',
     'MPC2K': 'MPC (Akai MPC 2k)',
     'MP3': 'MPEG-1/2 Audio',
     'OGG': 'OGG (OGG Container format)',
     'PAF': 'PAF (Ensoniq PARIS)',
     'PVF': 'PVF (Portable Voice Format)',
     'RAW': 'RAW (header-less)',
     'RF64': 'RF64 (RIFF 64)',
     'SD2': 'SD2 (Sound Designer II)',
     'SDS': 'SDS (Midi Sample Dump Standard)',
     'IRCAM': 'SF (Berkeley/IRCAM/CARL)',
     'VOC': 'VOC (Creative Labs)',
     'W64': 'W64 (SoundFoundry WAVE 64)',
     'WAV': 'WAV (Microsoft)',
     'NIST': 'WAV (NIST Sphere)',
     'WAVEX': 'WAVEX (Microsoft)',
     'WVE': 'WVE (Psion Series 3)',
     'XI': 'XI (FastTracker 2)'}
     ```