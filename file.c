// C++ implementation to delete a node
// in Binary Tree using Level Order Traversal

/*
Mulasfasfasfx

*/

#include <bits/stdc++.h>
using namespace std;

// Structure of Binary Tree
struct node {
    int data;
    node* left;
    node* right;
};

// Function to create new node
// of a Binary Tree.
node* newnode(int d)
{
    node* temp = new node;
    temp->data = d;
    temp->left = temp->right = NULL;
    return temp;
}

// Function for Level Order
// Traversal of Binary Tree
void levelorder(node* curr)
{

    // Queue to store the nodes
    // in a level
    queue<node*> q;
    if (curr)
        q.push(curr);

    // Loop to Traverse the Binary
    // Tree in Level Order
    while (!q.empty()) {
        curr = q.front();
        q.pop();
        cout << curr->data << " ";
        if (curr->left)
            q.push(curr->left);
        if (curr->right)
            q.push(curr->right);
    }
}

// Function to Delete the deepest
// right-most node of the Binary Tree
void deletedeepest(node* root,
                   node* temp)
{
    queue<node*> q;
    q.push(root);

    // Loop to Traverse Binary Tree
    // in level order and delete Node
    while (!q.empty()) {
        node* T = q.front();
        q.pop();
        if (T->right == temp) {
            T->right = NULL;
            delete (temp);
            return;
        }
        else
            q.push(T->right);
        if (T->left == temp) {
            T->left = NULL;
            delete (temp);
            return;
        }
        else
            q.push(T->left);
    }
}

// Function to Delete Node
// in Binary Tree
node* deletenode(node* root, int data)
{
    if (root == NULL)
        return NULL;

    // Condition if the Root node
    // is a leaf node.
    if (root->left == NULL
        && root->right == NULL) {
        if (root->data == data) {
            return NULL;
        }
        else
            return root;
    }
    queue<node*> q;
    q.push(root);
    node* temp = NULL;
    node* nodetodelete = NULL;

    // Loop to Traverse Tree in
    // Level Order and find the
    // Rightmost Deepest Node of the
    // Binary Tree and Node to be Deleted
    while (!q.empty()) {
        temp = q.front();
        q.pop();
        if (temp->data == data) {
            nodetodelete = temp;
        }
        if (temp->left) {
            q.push(temp->left);
        }
        if (temp->right) {
            q.push(temp->right);
        }
    }

    // if node to be deleted is not found
    if (nodetodelete != NULL) {

        // Condition to check if node to delete
        // is not same as node to replace
        if (temp != nodetodelete) {
            int t = temp->data;
            deletedeepest(root, temp);
            nodetodelete->data = t;
        }

        // if node to delete is also
        // rightmost deepest node
        else {
            deletedeepest(root, temp);
        }
    }
    return root;
}

// Driver Code
int main()
{

    // Construction of Tree
    node* root = newnode(1);
    root->left = newnode(8);
    root->right = newnode(3);
    root->left->left = newnode(4);
    root->left->right = newnode(5);
    root->right->left = newnode(6);
    root->right->right = newnode(7);

    cout << "Original Tree: ";
    levelorder(root);

    // Deleting node with key 8
    root = deletenode(root, 8);
    cout << endl;
    cout << "Deleting node with key 8: ";
    levelorder(root);

    // Deleting node with key 1
    root = deletenode(root, 1);
    cout << endl;
    cout << "Deleting node with key 1: ";
    levelorder(root);

    // Deleting node with key 4
    root = deletenode(root, 4);
    cout << endl;
    cout << "Deleting node with key 4: ";
    levelorder(root);
}