import csv
import re
import uuid


class Node:
	def __init__(self, children, isWord):
		self.children = children
		self.isWord = isWord


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
			current.isWord = True

	def autocomplete(self, prefix):
		current = self.trie
		for char in prefix:
			if not char in current.children:
				return []
			current = current.children[char]
		return self._findWordsFromNode(current, prefix)

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

	def bfs(self, visited, graph, node):
		visited.append(node)
		self.queue.append(node)

		while self.queue:
			s = self.queue.pop(0)
			print(s, end='')
			if graph.get(s) is not None:
				for neighbour in graph[s].children:
					if neighbour not in visited:
						visited.append(neighbour)
						self.queue.append(neighbour)

	def _findWordsFromNode(self, node, prefix):
		words = []
		if node.isWord:
			words += [prefix]
		for char in node.children:
			words += self._findWordsFromNode(node.children[char], prefix + char)
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
