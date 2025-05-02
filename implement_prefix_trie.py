class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr: TrieNode = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_word = True

    def search(self, word: str) -> bool:
        curr: TrieNode = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.is_word


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

    def print_trie(self) -> None:
        """Prints all the words currently stored in the Trie."""
        print("Words in Trie:")
        self._print_recursive(self.root, "")

    def _print_recursive(self, node: TrieNode, current_prefix: str) -> None:
        """Helper function to recursively traverse and print words."""
        # If the current node marks the end of a word, print it
        if node.is_word:
            print(f"- {current_prefix}")

        # Recursively call for all children, sorted for consistent output
        for char, child_node in sorted(node.children.items()):
            self._print_recursive(child_node, current_prefix + char)


# --- Test Execution Section ---


# The sequence of commands and their corresponding arguments
commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
arguments = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

# List to store the results of each operation
results = []

# The Trie object instance
trie_obj = None

# Iterate through the commands and arguments
for i in range(len(commands)):
    command = commands[i]
    args = arguments[i]

    if command == "Trie":
        trie_obj = Trie()
        results.append(None) # Constructor doesn't return a value in this context
    elif command == "insert":
        # Make sure trie_obj is initialized
        if trie_obj:
            result = trie_obj.insert(args[0]) # insert takes one argument: word
            results.append(result) # insert returns None
        else:
            results.append("Error: Trie not initialized")
    elif command == "search":
        # Make sure trie_obj is initialized
        if trie_obj:
            result = trie_obj.search(args[0]) # search takes one argument: word
            results.append(result)
        else:
            results.append("Error: Trie not initialized")
    elif command == "startsWith":
        # Make sure trie_obj is initialized
        if trie_obj:
            result = trie_obj.startsWith(args[0]) # startsWith takes one argument: prefix
            results.append(result)
        else:
            results.append("Error: Trie not initialized")
    else:
        results.append(f"Error: Unknown command '{command}'")

# Print the results
print(f"Commands: {commands}")
print(f"Arguments: {arguments}")
print(f"Results: {results}")

# --- Print Trie Content ---
if trie_obj:
    print("\n--- Trie Content ---")
    trie_obj.print_trie()
