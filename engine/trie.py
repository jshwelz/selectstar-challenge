import csv
import re
import uuid


class Node:
	def __init__(self, children, is_word):
		self.children = children
		self.is_word = is_word


class Tree:
	def __init__(self):
		self.trie = None
		self.queue = []

	def build(self, words):
		self.trie = Node({}, False)
		for word in words:
			current = self.trie
			for char in word:
				if not char in current.children:
					current.children[char] = Node({}, False)
				current = current.children[char]
			current.is_word = True

	def autocomplete(self, prefix):
		current = self.trie
		for char in prefix:
			if not char in current.children:
				return []
			current = current.children[char]
		return self.find_words_from_node(current, prefix)

	def dfs(self, visited, graph, node, word, words):
		if node not in visited:
			word += node
			if graph.get(node).isWord:
				words.append(word)
			visited.append(graph.get(node).children)
			if graph.get(node).children is not None:
				for neighbour in graph[node].children:
					self.dfs(visited, graph.get(node).children, neighbour, word, words)
		return words

	def find_words_from_node(self, node, prefix):
		words = []
		if node.is_word:
			words += [prefix]
		for char in node.children:
			words += self.find_words_from_node(node.children[char], prefix + char)
		return words


with open('engine/names.csv', newline='') as f:
	reader = csv.reader(f)
	data = list(reader)

Tree = Tree()
visited = []
flattened = [val for sublist in data for val in sublist]
Tree.build(flattened)
word = ''
words = []
sets = set()

for n in flattened:
	sets.add(re.split('[^a-zA-Z]', n)[0])

result = {'id': 'root', 'name': 'Tags', 'children': [{'id': uuid.uuid4(), 'name': s,
                                                      'children': [{'id': uuid.uuid4(), 'name': sh}
                                                                   for sh in Tree.autocomplete(s)]} for s in sets]}
