#include <bits/stdc++.h>
using namespace std;
struct node {
    int data;
    node* left;
    node* right;
};
node* newnode(int d)
{
    node* temp = new node;
    temp->data = d;
    temp->left = temp->right = NULL;
    return temp;
}
void levelorder(node* curr)
{
            queue<node*> q;
    if (curr)
        q.push(curr);
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
void deletedeepest(node* root,
                   node* temp)
{
    queue<node*> q;
    q.push(root);
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
node* deletenode(node* root, int data)
{
    if (root == NULL)
        return NULL;
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
        if (nodetodelete != NULL) {
                        if (temp != nodetodelete) {
            int t = temp->data;
            deletedeepest(root, temp);
            nodetodelete->data = t;
        }
                        else {
            deletedeepest(root, temp);
        }
    }
    return root;
}
int main()
{
        node* root = newnode(1);
    root->left = newnode(8);
    root->right = newnode(3);
    root->left->left = newnode(4);
    root->left->right = newnode(5);
    root->right->left = newnode(6);
    root->right->right = newnode(7);
    cout << "Original Tree: ";
    levelorder(root);
        root = deletenode(root, 8);
    cout << endl;
    cout << "Deleting node with key 8: ";
    levelorder(root);
        root = deletenode(root, 1);
    cout << endl;
    cout << "Deleting node with key 1: ";
    levelorder(root);
        root = deletenode(root, 4);
    cout << endl;
    cout << "Deleting node with key 4: ";
    levelorder(root);
}