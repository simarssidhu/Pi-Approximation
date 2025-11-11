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


@dataclass(frozen=True)
class PiApproxConfig:
    """Configuration matching the constants used in ``PiApprox.m``."""

    initial_value: mp.mpf = mp.mpf("1.01")
    exponent: int = 2
    iterations: int = 1000
    precision_digits: int = 1_000_000
    output_path: Path = Path("pi.txt")


def approximate_pi(config: PiApproxConfig) -> None:
    """Run the iterative approximation and persist the high-precision result."""

    # ``PiApprox.m`` performs the loop using double-precision arithmetic and
    # switches to ``digits(Precision)`` only after the iterations. To reproduce
    # that flow we run the loop with a moderate working precision and then
    # re-evaluate the final value at the requested digit count.
    mp.mp.dps = 50  # sufficient for the iterative phase
    x = mp.mpf(config.initial_value)

    for _ in range(config.iterations):
        x = mp.power(x, mp.power(config.exponent, mp.cos(x)))

    # After the loop the MATLAB code multiplies by two, raises the precision, and
    # displays the value with ``vpa``. ``mp.nstr`` lets us emit the same number of
    # digits.
    mp.mp.dps = config.precision_digits + 10  # guard digits for rounding
    result = mp.nstr(2 * x, n=config.precision_digits, strip_zeros=False)

    config.output_path.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    approximate_pi(PiApproxConfig())
