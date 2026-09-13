Convention: (channels, samples), transpose only at the classifier boundary
Synthetic board: fs 250, EEG rows 1–16, timestamp row 30
Baseline timing on synthetic data: mean dt 4.001 ms, std 0.251 ms, min/max 3.148/5.055 ms
Open question: how to timestamp on the real rig — MCU sample counter vs. host clock
Brainflow is not supported for the BioAmp pills. I must code a reader that pulls bytes off the ESP32's serial or BLE link and assembles them into the same (channels, samples) array shape.

bci/
├── pyproject.toml          ← dependencies + build config
├── NOTES.md                ← decisions log (you already started this)
├── .gitignore              ← must include data/
├── src/bci/
│   ├── __init__.py
│   ├── acquisition/
│   │   ├── __init__.py
│   │   ├── source.py       ← the contract
│   │   ├── synthetic.py    ← fake EMG
│   │   └── serial_esp32.py ← empty until Phase 1
│   ├── buffer.py
│   ├── dsp/
│   └── decoding/
├── scripts/
│   └── smoke_acquire.py    ← things you run by hand
├── tests/
└── data/                   ← gitignored, recordings live here
