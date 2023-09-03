import logging
from typing import Type
import pytest
from rdflib import Dataset, Graph, Namespace

EGSCHEME = Namespace("example:")

QUERY = r"""
SELECT ?s ?p ?o WHERE
{
    ?s ?p ?o .
}
"""

DATA = f"<{EGSCHEME.s}> <{EGSCHEME.p}> <{EGSCHEME.o}> ."


@pytest.mark.parametrize(
    ("store", "graph_type"),
    [
        ("Oxigraph", Dataset),
        (..., Dataset),
        ("Oxigraph", Graph),
        (..., Graph),
    ],
)
def test_query(store: str, graph_type: Type[Graph]):
    if store == "Oxigraph":
        graph = graph_type(store=store)
    else:
        graph = graph_type()

    if isinstance(graph, Dataset):
        graph.default_context.parse(data=DATA, format="ntriples")
        logging.debug(f"{graph.default_context.identifier = }")
    else:
        graph.parse(data=DATA, format="ntriples")
    logging.debug(f"{graph.identifier = }")

    result = graph.query(QUERY)

    rows = list(result)
    assert rows == [
        (EGSCHEME.s, EGSCHEME.p, EGSCHEME.o),
    ]


# print("Dataset")
# ds = Dataset()
# ds.default_context.parse(data=data, format="ntriples")

# qres = ds.query(query)
# for row in qres:
#     print(row)

# print("Dataset(store=\"Oxigraph\")")
# ds = Dataset(store="Oxigraph")
# ds.default_context.parse(data=data, format="ntriples")

# qres = ds.query(query)
# for row in qres:
#     print(row)
