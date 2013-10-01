public_library
==============

CF challenge #1: Model of a public library. 

I came up with two ways of modeling a library, both of which are in progress... I am currently trying to reconcile them. The PRETTY_public_library, which isn't terribly pretty, has a nicer output when you try to list books. However, I was only able to accomplish this nicer appearance by storing just the book.titles (vs. the objects themselves) inside the shelves/library. In constrast, the ACCURATE_public_library stores the book objects themselves inside the shelves/library, but they don't list prettily... yet. 

Once I figure out how to reconcile these two approaches, I will update the enshelf and unshelf methods to shelve and unshelve books based on their authors (i.e., the methods will know where to locate the books based on the authors' last names). 
