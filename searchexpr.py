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