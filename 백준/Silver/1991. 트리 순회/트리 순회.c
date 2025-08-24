#include <stdio.h>
#include <stdlib.h>

typedef struct _node 
{
    char data;
    struct _node* left;
    struct _node* right;
}Node;

typedef struct bintree
{
    Node* root;
}BinTree;

BinTree* make_BinTree()
{
    BinTree* new_Bintree = (BinTree*)malloc(sizeof(BinTree));
    new_Bintree->root = NULL;
    
    return new_Bintree;
}

Node* new_node(char data, Node* left_child, Node* right_child) 
{
    Node* new_node = (Node*)malloc(sizeof(Node));

    new_node->data = data;
    new_node->left = left_child;
    new_node->right = right_child;

    return new_node;
}

Node* find(char target, Node* root) 
{
    if (root == NULL) return NULL;
    if (root->data == target) return root;
    
    Node* left_search = find(target, root->left);
    if (left_search != NULL) return left_search;
    return find(target, root->right);
}

void insert(BinTree* bintree, char parent,
    char left_child, char right_child) 
{
    Node* p = find(parent, bintree->root);
    
    if (left_child != '.') p->left = new_node(left_child, NULL, NULL);
    if (right_child != '.') p->right = new_node(right_child, NULL, NULL);
}

void preorder_traversal(Node* root) 
{
    if (root) {
        printf("%c", root->data);
        preorder_traversal(root->left);
        preorder_traversal(root->right);
    }
}

void inorder_traversal(Node* root) 
{
    if (root) {
        inorder_traversal(root->left);
        printf("%c", root->data);
        inorder_traversal(root->right);
    }
}

void postorder_traversal(Node* root) 
{
    if (root) {
        postorder_traversal(root->left);
        postorder_traversal(root->right);
        printf("%c", root->data);
    }
}

void delete_all_node(Node* node) 
{
    if (node) {
        delete_all_node(node->left);
        delete_all_node(node->right);
        free(node);
    }
}

void delete_bintree(BinTree* bintree) 
{
    delete_all_node(bintree->root);
    free(bintree);
}

int main()
{
    int N;
    scanf("%d", &N);

    BinTree* new_bintree = make_BinTree();

    for (int i = 0; i < N; i++) 
    {
        char parent, left_data, right_data;
        scanf(" %c %c %c", &parent, &left_data, &right_data);

        if (parent == 'A') new_bintree->root = new_node(parent, NULL, NULL);
        insert(new_bintree, parent, left_data, right_data);
    }

    preorder_traversal(new_bintree->root); printf("\n");
    inorder_traversal(new_bintree->root); printf("\n");
    postorder_traversal(new_bintree->root); printf("\n");

    delete_bintree(new_bintree);

    return 0;
}