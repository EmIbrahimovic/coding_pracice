#include <iostream>
#include <vector>
#include <map>
#include <utility>

using namespace std;

template <typename T>
struct AVLTree {
    T value;
    AVLTree *parent;
    AVLTree *left, *right;
    int depth = 0;

    AVLTree() {
        this->parent = AVLTree()
    }
    void insert(T val);
    void delete(T val);
    void getSuffixMin(int index);
};


template <typename T>
void AVLTree<T>::insert(T val) {
    return 0;
}


int main() {




    return 0;
}
