from doctest import ELLIPSIS

import pytest
import torch
from matplotlib import pyplot as plt
from sybil import Sybil
from sybil.parsers.myst import DocTestDirectiveParser, PythonCodeBlockParser

import dynamiqs


# doctest fixture
@pytest.fixture(scope='session', autouse=True)
def torch_set_printoptions():
    torch.set_printoptions(precision=3, sci_mode=False)


# doctest fixture
@pytest.fixture(scope='session', autouse=True)
def mplstyle():
    dynamiqs.plots.utils.mplstyle()


# doctest fixture
@pytest.fixture()
def render():
    def savefig_docs(figname):
        filename = f'docs/figs-docs/{figname}.png'
        plt.gcf().savefig(filename, bbox_inches='tight')

    return savefig_docs


# sybil configuration
pytest_collect_file = Sybil(
    parsers=[
        DocTestDirectiveParser(optionflags=ELLIPSIS),
        PythonCodeBlockParser(),
    ],
    patterns=['*.md'],
    fixtures=['render'],
).pytest()
