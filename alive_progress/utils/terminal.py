import sys
from functools import partial


def _send_ansi_escape(*sequence):  # pragma: no cover
    return partial(sys.__stdout__.write, ''.join(f'\x1b[{s}' for s in sequence))


if sys.stdout.isatty():
    clear_traces = _send_ansi_escape('2K\r')  # clears the entire line: CSI n K -> with n=2.
    hide_cursor = _send_ansi_escape('?25l')  # hides the cursor: CSI ? 25 l.
    show_cursor = _send_ansi_escape('?25h')  # shows the cursor: CSI ? 25 h.
else:
    clear_traces = hide_cursor = show_cursor = lambda: None