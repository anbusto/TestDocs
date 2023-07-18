class testClass():
    """This class identifies sequences of anomalous spectra.

    This algorithm assumes that the background environment will be consistent over known timescales.
    I.e., this algorithm is only intended for static detector, mobile source scenarios.

    """

    def __init__(self, long_term_duration: int = 120, short_term_duration: int = 1,
                 pre_event_duration: int = 5, max_event_duration: float = 120,
                 post_event_duration: int = 1.5, tolerable_false_alarms_per_day: float = 1.0,
                 anomaly_threshold_update_interval: float = 60):
        """Initializes an event detector object."""

        print("hello test")
