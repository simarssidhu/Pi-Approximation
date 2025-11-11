"""Python port of the ``PiApprox.m`` script.

The MATLAB code:

* Starts with ``x = 1.01``.
* Iteratively applies ``x = x^((Exponent)^(cos(x)))`` for ``Max_Iter`` updates.
* Doubles the final ``x`` and prints it with ``Precision`` digits using ``vpa``.
* Writes the high-precision value into ``pi.txt`` via ``diary``.

This module mirrors that behaviour using :mod:`mpmath` so that we can request
over one million digits of precision for the final result, as required.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mpmath import mp

try:  # ``set_backend`` is only present in newer mpmath releases.
    from mpmath.libmp import set_backend
except ImportError:  # pragma: no cover - gracefully handle older versions
    set_backend = None
else:  # pragma: no cover - exercise when the helper exists
    try:  # pragma: no cover - ``gmpy2`` accelerates multiprecision arithmetic
        import gmpy2  # type: ignore
    except ImportError:
        pass
    else:
        set_backend("gmpy")


@dataclass(frozen=True)
class PiApproxConfig:
    """Configuration matching the constants used in ``PiApprox.m``."""

    initial_value: mp.mpf = mp.mpf("1.01")
    exponent: int = 2
    iterations: int = 1000
    precision_digits: int = 1_000_000
    guard_digits: int = 50
    output_path: Path = Path("pi.txt")


def approximate_pi(config: PiApproxConfig) -> None:
    """Run the iterative approximation and persist the high-precision result."""

    # ``PiApprox.m`` relies on MATLAB's variable-precision arithmetic to carry
    # millions of digits when ``digits(Precision)`` is invoked.  We mirror that
    # behaviour by running the entire iterative phase with the full requested
    # precision so the accumulated value retains all available digits.
    mp.dps = config.precision_digits + config.guard_digits
    x = mp.mpf(config.initial_value)
    base = mp.mpf(config.exponent)

    for _ in range(config.iterations):
        cos_x = mp.cos(x)
        x = mp.power(x, mp.power(base, cos_x))

    result = mp.nstr(2 * x, n=config.precision_digits, strip_zeros=False)

    config.output_path.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    approximate_pi(PiApproxConfig())
