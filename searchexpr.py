from enum import Enum
from typing import List, Dict, Union

class taggeditem:
    def __init__(this, obj, tags : List[str]):
        this.obj = obj
        this.tags : List[str] = tags
    
    def __str__(this) -> str:
        return ", ".join(this.tags)
    
    def contains(this, tag : str) -> bool:
        return len(list(filter(lambda t: t == tag, this.tags))) > 0
    
    def containsany(this, tags : List[str]) -> bool:
        for tag in tags:
            if this.contains(tag):
                return True
        return False
    
    def containsall(this, tags : List[str]) -> bool: 
        for tag in tags:
            if not this.contains(tag):
                return False
        return True


class taggeditemset:
    def __init__(this, items : List[taggeditem]):
        this.items : List[taggeditem] = items

    def contain(this, tag : str) -> filter:
        return filter(lambda titem: titem.contains(tag), this.items)

    def containany(this, tags : List[str]) -> filter:
        return filter(lambda titem: titem.containsany(tags), this.items)

    def containall(this, tags : List[str]) -> filter:
        return filter(lambda titem: titem.containsall(tags), this.items)

class basicop(Enum):
    AND = "&" 
    OR = "|"
    UNION = "+"
    DISJOINT = "-"

class searchexpr:
    def __init__(this, expr : str, itemset : taggeditemset):
        this.expr = expr
        this.setref = itemset
    
    def structurize(this, expr : str):
        struct = []
        for op in [basicop.UNION.value, basicop.DISJOINT.value, basicop.OR.value, basicop.AND.value]:
            if op in expr and len(expr) > 1:
                struct = [op] + expr.split(op, maxsplit=1) # maxsplit = 1 => only pairwise operations
                for i in range(len(struct)):
                    struct[i] = this.structurize(struct[i])
                return struct
        return expr.strip().lower()

    def issimple(this, structure : list):
        for item in structure:
            if isinstance(item, list):
                return False
        return True

    def op2filter(this, structure : list): 
        for i in range(len(structure)):
            if isinstance(structure[i], list):
                structure[i] = this.op2filter(structure[i])


        # bug: for "tag1 & tag2 | tag3"
        #       the search is only conducted on items that already
        #       fulfill "tag1 & tag2"
        if this.issimple(structure):
            if structure[0] == basicop.UNION.value:
                pass
            elif structure[0] == basicop.DISJOINT.value:
                pass
            elif structure[0] == basicop.OR.value:
                if isinstance(structure[1], filter) and isinstance(structure[2], filter):
                    structure = filter(lambda it: True, set(list(structure[1]) + list(structure[2])))
                else:
                    structure = this.setref.containany(structure[1:]) 
            elif structure[0] == basicop.AND.value:
                if isinstance(structure[1], filter):
                    structure = taggeditemset(list(structure[1])).contain(structure[2])
                elif isinstance(structure[2], filter):
                    structure = taggeditemset(list(structure[2])).contain(structure[1])
                else:
                    structure = this.setref.containall(structure[1:])

        return structure


    def decompose(this):
        # every expression is either a simple expression,
        # i.e. can be evaluated by contains / containsall, containsany
        # or it is a basic expression combining two operands, 
        # of which at least one is another searchexpr
        structure = this.structurize(this.expr) 
        # now everything is structured into lists of three: op and two operands
        filt = this.op2filter(structure)
        # now simple expressions are replaced by filters
        results = list(filt)

        return results