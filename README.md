# textprocessor
A repository to develop a textprocessor, aiming to feature a search prompt parser in the future. Implemented in Python as sketch of concept.

Start with implementing simple text-structuring features first to define some basic syntax. Then continue with logical search expressions.

An example could be a set of items tagged by tags from ["tag1", "tag2", "tag3", "tag4"] and to implement "(", ")", "|", "&", "-" and "+". These should represent operations on subsets on a set of items to identify search results.
"+" would then define a union of sets, "-" a disjunction, while "|" represents the subset of all items containing one tag *or* the other, while "&" does the same for *and*.

Expressions would then look roughly like

* "tag1 | tag2"
* "tag2 -tag2"
* "tag1 & ( tag2 | tag3 )"
* "tag1 | tag2 + tag3 | tag4"
* "tag1 | tag2 - tag3"

and so on.