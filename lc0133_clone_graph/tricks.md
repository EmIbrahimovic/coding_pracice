---
strongly-connected:
- "[[simple graph]]"
- "[[oop]]"
---

# LeetCode 5. Longest Plaindromic Substring

ideja: ici bfs-om
imati niz pointera na node-ove tako da znamo koji index je koji node
kad naletimo na novi node u necijem adjacency-u, tad napravimo novi u ovoj listi
dok prolazimo kroz neciju listu, popunjavamo listu tog cvora.

standardni bfs.

## approach lessons

bfs funkcionise.
samo runnaj 3 put svaki submission. spalo mi je sa 6ms u 0ms nakon sto sam drugi put submittala.

neki ljudi su ga radili i rekurzivno sto definitivno ima smisla. samo moras moc visited ocuvati.

## cpp code optimization lessons

* [[dynamic allocation]] - ako dinamicno alociras objekt sa 
```
Node* ptr = new Node();
```
onda ce ti se objekt sacuvat i izvan funkcije
* [[static allocation]] - ako staticno alociras sa
```
Node node = Node();
Node* ptr = &node;
```
`node` se brise izvan funkcije i ti ako returnas taj `ptr`, on ce pokazivati
na prazan prostor

alocijranje niza pointera je brze nego alociranje niza objekata. 
s tim da je ovaj node poprilicno mal, samo int i pointer na vector koji je negdje
