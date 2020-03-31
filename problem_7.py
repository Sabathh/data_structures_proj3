from typing import List

class RouteTrie:
    def __init__(self, root_handler: str):
        """ Initializes the trie with a root node and a handler, this is the root path 
        
        Arguments:
            root_handler {str} -- Handler to be stored at the root level
        """
        self.root = RouteTrieNode()
        self.root_handler = root_handler

    def insert(self, path_list: List[str], handler: str):
        """ Traverses the Trie and adds inserts the handler at the end of the specified path

            Time complexity: O(n), where n is the number of items in path_list

            Space complexity: O(n). Number of nodes created scales linearly with the size of path_list
        
        Arguments:
            path_list {List[str]} -- Path broken down into a list
            handler {str} -- Handler to be stored at the specified path
        """
    
        current_node = self.root

        if len(path_list) == 0:
            return

        # Navigate the Trie using the path provided. 
        # If part of the path does not exist in the Trie a node will be created
        for path in path_list:
            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler

    def find(self, path_list: List[str]) -> str:
        """ Starting at the root, navigate the Trie to find a match for this path

            Time complexity: O(n), where n is the number of items in path_list

            Space complexity: O(1). Space used is independent of the inputs.
        
        Arguments:
            path_list {List[str]} -- Path broken down into a list
        
        Returns:
            str -- If a match is found returns the equivalent RouteTrieNode.handler.
                   Otherwise, returns None.
        """
        
        if len(path_list) == 0:
            return self.root_handler

        current_node = self.root

        # Navigate the Trie using the path provided. 
        # If part of the path does not exist, stop the search.
        for path in path_list:
            if path in current_node.children:
                current_node =  current_node.children[path]
            else:
                return None

        return current_node.handler


class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, path : str):
        """ Insert node for the provided path
        
        Arguments:
            path {str} -- Path for the node
        """
        if path not in self.children:
            self.children[path] = RouteTrieNode()


class Router:
    def __init__(self, root_handler: str, not_found_handler: str):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path_str: str, handler: str):
        """ Adds a handler for the specified path
        
        Arguments:
            path_str {str} -- Full path
            handler {str} -- Handler to be added to the path
        """
        
        path_list = self.split_path(path_str)
        self.route_trie.insert(path_list, handler)


    def lookup(self, path_str: str) -> str:
        """ Attempts to retrieve a handler from the specified path
        
        Arguments:
            path_str {str} -- Full path
        
        Returns:
            str -- If a match is found returns the equivalent RouteTrieNode.handler.
                   Otherwise, returns self.not_found_handler.
        """
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
        """ Splits the path into a list so it can be iterated onto.
        
        Arguments:
            path_str {str} -- Full path
        
        Returns:
            List[str] -- List containing the individual paths in the order they were specified
        """

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