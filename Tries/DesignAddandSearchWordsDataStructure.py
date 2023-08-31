from trie import TrieNode


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                cur_node.children[c] = TrieNode()
                cur_node = cur_node.children[c]
        cur_node.is_word = True

    def search(self, word: str) -> bool:
        cur_node = self.root

        def dfs(i, cur_node):
            if i >= len(word):
                return cur_node.is_word

            if word[i] == ".":
                for val in cur_node.children.values():
                    if dfs(i + 1, val):
                        return True
                return False

            if word[i] not in cur_node.children:
                return False

            return dfs(i + 1, cur_node.children[word[i]])

        return dfs(0, cur_node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == "__main__":
    cmds = [
        "WordDictionary",
        "addWord",
        "addWord",
        "addWord",
        "search",
        "search",
        "search",
        "search",
    ]
    words = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    # [null,null,null,null,false,true,true,true] correct output TODO have to fix code not giving correct output
    print(f"Input: commands: {cmds}\nwords: {words}")
    sol = None
    res = []
    for i, cmd in enumerate(cmds):
        output = None
        if cmd == "WordDictionary":
            sol = WordDictionary()
        elif cmd == "addWord":
            sol.addWord(words[i])
        elif cmd == "search":
            output = sol.search(words[i])
        res.append(output)

    print(f"Output: {res}")
