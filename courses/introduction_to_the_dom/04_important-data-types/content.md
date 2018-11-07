This reference tries to describe the various objects and types in simple terms. But there are a number of different data types being passed around the API that you should be aware of. For the sake of simplicity, syntax examples in this API reference typically refer to nodes as elements, to arrays of nodes as nodeLists (or simply elements), and to attribute nodes simply as attributes.

The following table briefly describes these data types.

| Data type | Description |
| --- | --- |
| Document |	When a member returns an object of type document (e.g., the ownerDocument property of an element returns the document to which it belongs), this object is the root document object itself. The [DOM `document` Reference](https://developer.mozilla.org/en-US/docs/Web/API/Document) chapter describes the document object. |
| Element |	element refers to an element or a node of type element returned by a member of the DOM API. Rather than saying, for example, that the document.createElement() method returns an object reference to a node, we just say that this method returns the element that has just been created in the DOM. element objects implement the DOM Element interface and also the more basic Node interface, both of which are included together in this reference. |
| NodeList |	A nodeList is an array of elements, like the kind that is returned by the method document.getElementsByTagName(). Items in a nodeList are accessed by index in either of two ways: `list.item(1)` or `list[1]`. These two are equivalent. In the first, item() is the single method on the nodeList object. The latter uses the typical array syntax to fetch the second item in the list. |
| Attribute |	When an attribute is returned by a member (e.g., by the createAttribute() method), it is an object reference that exposes a special (albeit small) interface for attributes. Attributes are nodes in the DOM just like elements are, though you may rarely use them as such. |
| NamedNodeMap |	A namedNodeMap is like an array, but the items are accessed by name or index, though this latter case is merely a convenience for enumeration, as they are in no particular order in the list. A namedNodeMap has an item() method for this purpose, and you can also add and remove items from a namedNodeMap. |

