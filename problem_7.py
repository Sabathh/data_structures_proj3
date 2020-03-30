from typing import List
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler: str):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root_handler = root_handler

    def insert(self, path_list: List[str], handler: str):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        if len(path_list) == 0:
            return

        for path in path_list:
            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler

    def find(self, path_list: List[str]) -> str:
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        if len(path_list) == 0:
            return self.root_handler

        current_node = self.root

        for path in path_list:
            if path in current_node.children:
                current_node =  current_node.children[path]
            else:
                return None

        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, handler : str):
        # Insert the node as before
        if handler not in self.children:
            self.children[handler] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler: str, not_found_handler: str):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path_str: str, handler: str):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path_str)
        self.route_trie.insert(path_list, handler)


    def lookup(self, path_str: str) -> str:
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        path_list = self.split_path(path_str)
        handler = self.route_trie.find(path_list)

        if handler is None:
            return self.not_found_handler
        else:
            return handler


    def split_path(self, path_str: str) -> List[str]:
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        path_list = [path for path in path_str.split("/") if path != ""]

        return path_list

def test_edge_cases():
    edge_router = Router("root handler", "not found handler")

    # Attempt to modify root handler. Assumed root handler cannot be modified
    edge_router.add_handler("/", "about handler")  
    assert(edge_router.lookup("/") == "root handler")

    # Path that does not start with "/""
    edge_router.add_handler("/home/about", "about handler")
    assert(edge_router.lookup("home/about") == "about handler")

    # Long path
    edge_router.add_handler("/home/the/bird/is/the/word/dont/you/know/about/the/bird", "Surfin' Bird")
    assert(edge_router.lookup("/home/the/bird/is/the/word/dont/you/know/about/the/bird") == "Surfin' Bird")

def test_regular_cases():
    router = Router("root handler", "not found handler")
    
    router.add_handler("/home/about", "about handler")  
    router.add_handler("/home/usr/sabath", "sabath handler")  
    router.add_handler("/home/usr/skai", "skai handler")  
    router.add_handler("/home/usr/skai", "skai handler")  
    router.add_handler("/dev/src/code", "source handler") 
    
    assert(router.lookup("/") == "root handler") 
    assert(router.lookup("/home") == "not found handler") 
    assert(router.lookup("/home/about") == "about handler") 
    assert(router.lookup("/home/about/") == "about handler") 
    assert(router.lookup("/home/about/me") == "not found handler") 
    
    assert(router.lookup("/") == "root handler") 
    assert(router.lookup("/home") == "not found handler") 
    assert(router.lookup("/home/usr") == "not found handler") 
    assert(router.lookup("/home/usr/sabath") == "sabath handler")
    assert(router.lookup("/home/usr/skai") == "skai handler")
    assert(router.lookup("/dev") == "not found handler")  
    assert(router.lookup("/dev/src") == "not found handler")  
    assert(router.lookup("/dev/src/code") == "source handler") 

if __name__ == "__main__":
    test_edge_cases()
    test_regular_cases()