#include <string>
#include <queue>
#include <iostream>
#include <vector>
#include "utils.h"

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};


class Solution {
public:

    vector<Node> nodes;

    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;

        nodes.clear();
        nodes.assign(101, Node(0));

        Node* root = &nodes[1];
        root->val = 1;

        queue<Node*> q; // This will have nodes from the actual graph
        q.push(node);

        while (!q.empty()) {
            Node* u = q.front();
            q.pop();
            Node* u_copy = &nodes[u->val];

            for (auto v : u->neighbors) {
                int v_val = v->val;

                if (nodes[v_val].val == 0) {
                    nodes[v_val].val = v_val;
                    q.push(v);
                }
                Node* v_copy = &nodes[v_val];

                (u_copy->neighbors).push_back(v_copy);
            }
        }

        return root;
    }
};

int main() {

    Solution sol;

    vector<Node> nodes(5, Node(0));
    for (int i = 1; i <= 5; i++) nodes[i].val = i;
    
    nodes[1].neighbors = {&nodes[2], &nodes[4]};
    nodes[2].neighbors = {&nodes[1], &nodes[3]};
    nodes[3].neighbors = {&nodes[2], &nodes[4]};
    nodes[4].neighbors = {&nodes[1], &nodes[3]};

    cout << "Actual graph addresses" << endl;
    for (int i = 1; i < 5; i++) cout << &nodes[i] << " ";
    cout << endl;

    Node* root_copy = sol.cloneGraph(&nodes[1]);
    cout << root_copy << endl;

    return 0;
}
