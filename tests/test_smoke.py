import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

board_id = BoardIds.SYNTHETIC_BOARD
fs = BoardShim.get_sampling_rate(board_id)
eeg_rows = BoardShim.get_eeg_channels(board_id)
ts_row = BoardShim.get_timestamp_channel(board_id)
print(f"fs = {fs} Hz")
print(f"eeg rows = {eeg_rows}")
print(f"timestamp row = {ts_row}")

DURATION = 5.0
board = BoardShim(board_id, BrainFlowInputParams())
board.prepare_session()
board.start_stream()
time.sleep(DURATION)
data = board.get_board_data()
board.stop_stream()
board.release_session()

print("array shape:", data.shape)
print(f"samples: {data.shape[1]}  |  expected ~{int(fs * DURATION)}")

ts = data[ts_row, :]
dt = np.diff(ts)
print(f"mean dt = {dt.mean()*1000:.3f} ms  |  implied fs = {1/dt.mean():.2f} Hz")
print(f"dt std = {dt.std()*1000:.3f} ms  |  min/max = {dt.min()*1000:.3f}/{dt.max()*1000:.3f} ms")