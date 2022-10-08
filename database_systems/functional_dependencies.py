def get_group_closure(x: set, f: dict[frozenset:set]) -> set:
    """
    Find the closure of a group (x), a subset of a relation schema (r), using a group of functional dependencies (f).
    """
    xc = x.copy()
    fc = f.copy()
    c = True
    while c:
        cc = False
        for k, v in fc.items():
            if k.issubset(xc) and not v.issubset(xc):
                cc = True
                xc = xc.union(v)
                fc.pop(k)
                break
        if not cc:
            c = False
    return xc


def find_whether_dep_is_derived_from_deps_group():
    pass


def get_functional_dependencies_group_closure():
    pass


def find_candidate_keys():
    pass


def find_canonical_cover():
    pass


def is_extraneous_attribute():
    pass


def decomposition_to_3nf():
    pass


def decomposition_to_bcnf():
    pass


print(get_group_closure({'A', 'B'}, {frozenset({'A'}): {'C', 'D'},
                                     frozenset({'B'}): {'E'},
                                     frozenset({'C'}): {'A', 'E'}}))
