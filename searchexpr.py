from typing import List, Dict, Union

class taggeditem:
    def __init__(this, obj, tags : List[str]):
        this.obj = obj
        this.tags : List[str] = tags
    
    def contains(this, tag : str) -> bool:
        return (len(list(filter(lambda t: t == tag, this.tags))))

class taggeditemset:
    def __init__(this, items : List[taggeditem]):
        this.items : List[taggeditem] = items

    def contain(this, tag : str) -> filter:
        return filter(lambda titem: titem.contains(tag), this.items)
