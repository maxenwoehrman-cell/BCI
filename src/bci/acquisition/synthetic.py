import numpy as np


class SyntheticEMGSource:
    """Generates fake 2-channel forearm EMG for pipeline development."""

    GESTURES = {
        "REST":         (0.0, 0.0),
        "FIST":         (1.0, 0.3),
        "OPEN":         (0.2, 1.0),
        "WRIST_FLEX":   (0.9, 0.5),
        "WRIST_EXTEND": (0.4, 0.9),
    }

    def __init__(self, fs=2000.0, n_channels=2, seed=0, reps=20, cue_dur=3.0):
        self.fs = fs
        self.n_channels = n_channels
        self.cue_dur = cue_dur

        self._rng = np.random.default_rng(seed)

        labels = list(self.GESTURES) * reps
        order = self._rng.permutation(len(labels))
        self._schedule = [
            (i * cue_dur, (i + 1) * cue_dur, labels[j])
            for i, j in enumerate(order)
        ]

        self._t0 = None
        self._last_read = None
        self._n_emitted = 0

    @property
    def cues(self):
        """Ground-truth cue log: list of (t_start, t_end, label)."""
        return list(self._schedule)

    def start(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError