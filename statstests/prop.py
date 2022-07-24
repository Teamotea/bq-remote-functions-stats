from typing import Any
from dataclasses import dataclass
from statsmodels.stats.proportion import proportions_ztest


@dataclass
class SingleProportion:
    successes: int
    trials: int


@dataclass
class PropTestResult:
    result: list[str]


def test(calls: list[list[Any]]) -> PropTestResult:
    assert len(calls) == 2
    p1 = SingleProportion(calls[0][0], calls[0][1])
    p2 = SingleProportion(calls[1][0], calls[1][1])
    count = [p1.successes, p2.successes]
    nobs = [p1.trials, p2.trials]
    stat, pval = proportions_ztest(count, nobs)
    result = PropTestResult([
        f'Statistic: {stat:.4f}. Pval: {pval:.6f}.',
        None
    ])
    return result
