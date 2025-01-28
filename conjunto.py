#!/usr/bin/env python3

print(1)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
print(conjunto1.union(conjunto2))

print(2)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
conjunto1.union(conjunto2)
print(conjunto1)

print(3)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
print(conjunto1.add("grafite"))

print(4)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
conjunto1.add("grafite")
print(conjunto1)

print(5)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
conjunto1.update(conjunto2)
print(conjunto1)

print(6)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
conjunto1.remove("lápis")
print(conjunto1)

print(7)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
conjunto1.discard("lápis")
print(conjunto1)

print(8)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
conjunto1.pop()
print(conjunto1)

print(9)
conjunto1 = {"lápis", "borracha", "apontador"}
conjunto2 = {"lápis", "caneta", "marcador"}
print(conjunto1.pop())
