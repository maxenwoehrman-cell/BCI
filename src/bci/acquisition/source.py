from typing import Protocol
import numpy as np


class Source(Protocol):
    """Contract for anything that produces biopotential samples.

    Implementations: SyntheticEMGSource (Phase 0), SerialESP32Source (Phase 1).
    """

    fs: float
    n_channels: int

    def start(self) -> None:
        """Begin acquisition. After this, time is running."""
        ...

    def read(self) -> np.ndarray:
        """Return every sample acquired since the previous call.

        Shape (n_channels, n_new), oldest sample first. n_new varies
        per call and may be 0. Non-blocking.
        """
        ...

    def stop(self) -> None:
        """Release resources. Idempotent."""
        ...