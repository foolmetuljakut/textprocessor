from searchexpr import taggeditem, taggeditemset

if __name__ == "__main__":
    taglist = [
        ["tag1"],
        ["tag1", "tag2"],
        ["tag1", "tag3"],
        ["tag2", "tag3"],
        ["tag1", "tag2", "tag3"],
    ]
    s = taggeditemset(list(map(lambda tlist: taggeditem(None, tlist), taglist)))
    f = list(s.contain("tag2"))
    print()
