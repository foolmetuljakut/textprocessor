from searchexpr import taggeditem, taggeditemset, searchexpr

if __name__ == "__main__":
    taglist = [
        ["tag1"],
        ["tag1", "tag2"],
        ["tag1", "tag3"],
        ["tag2", "tag3"],
        ["tag1", "tag2", "tag3"],
        ["tag1", "tag2", "tag3", "tag4"],
    ]
    s = taggeditemset(list(map(lambda tlist: taggeditem(None, tlist), taglist)))

    f = list(s.contain("tag2"))
    g = list(s.containall(["tag2", "tag1"]))
    h = list(s.containany(["tag2", "tag1"]))

    expr = searchexpr("tag1 & tag2 | tag3", s)
    print(list(map(lambda titem: str(titem.tags), expr.decompose())))

    expr = searchexpr("tag1 & tag2 | tag3 & tag4", s)
    print(list(map(lambda titem: str(titem.tags), expr.decompose())))

    # continue with https://stackoverflow.com/a/35445045
    print()
