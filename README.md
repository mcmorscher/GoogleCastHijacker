# Google Cast Hijacker
## Introduction to Computer Security Final Project, Michael Morscher

This is a proof-of-concept script which "hijacks" all Google Cast-enabled speakers and televisions on a network by playing Never Gonna Give You Up by Rick Astley.

#### Instructions
* How to run: `python hijack.py`
* This will search for all discoverable Google Cast devices and return a numbered list of the devices
* To hijack one or more devices, when prompted enter a space-separated list of device numbers (eg. `1 2 4`) or `a` to hijack all devices
* The script will print a message indicating whether the hijacking was successful

#### Dependencies
Third-party Python Libraries
* pychromecast
* youtube_dl

#### Disclaimer
This project is intended to raise awareness about how the open discoverability and connectability of Google Cast devices enables exploitability on shared networks. It is for educational purposes only. The author encourages responsible use and does not promote the "hijacking" of devices without consent.
