# Node dasar dari Trie
class TrieNode:
    def __init__(self):
        self.children = {}      # Dictionary untuk menyimpan child node berdasarkan karakter
        self.is_end_of_word = False  # Menandakan apakah node ini akhir dari sebuah kata


# Struktur data Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node kosong untuk memulai Trie

    # ----------------------------
    # MENAMBAHKAN KATA KE DALAM TRIE
    # ----------------------------
    def insert(self, word):
        node = self.root  # Memulai dari root
        for char in word:  # Iterasi karakter demi karakter dari kata yang dimasukkan
            if char not in node.children:  # Jika karakter belum ada di node saat ini
                node.children[char] = TrieNode()  # Buat node baru untuk karakter tersebut
            node = node.children[char]  # Pindah ke node karakter berikutnya

        node.is_end_of_word = True  # Menandai akhir kata

    # ----------------------------
    # MENCARI KATA DI DALAM TRIE
    # ----------------------------
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:  # Jika karakter tidak ditemukan
                return False
            node = node.children[char]  # Pindah ke node berikutnya

        return node.is_end_of_word  # True jika kata ditemukan lengkap

    # ----------------------------
    # MENCARI SEMUA KATA DENGAN PREFIX TERTENTU
    # ----------------------------
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:  # Telusuri berdasarkan prefix
            if char not in node.children:
                return []  # Jika prefix tidak ada, kembalikan list kosong
            node = node.children[char]

        # Jika prefix ditemukan, kumpulkan semua kata dari node ini
        result = []
        self._collect_words(node, prefix, result)
        return result

    # Helper (fungsi pembantu untuk mengambil semua kata dari node tertentu)
    def _collect_words(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)

        for char, next_node in node.children.items():
            self._collect_words(next_node, prefix + char, result)


# --------------------------------------------
# CONTOH PENGGUNAAN TRIE
# --------------------------------------------
trie = Trie()
trie.insert("car")
trie.insert("cat")
trie.insert("care")
trie.insert("dog")

print(trie.search("car"))     # True
print(trie.search("car"))     # False
print(trie.starts_with("ca"))  # ['car', 'care', 'cat']
print(trie.starts_with("d"))