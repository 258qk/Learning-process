#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int val;
    struct Node *next;
}Node;

void create_chain(Node **head,Node **tail,int val)
{
        Node *n = (Node*)malloc(sizeof(Node));
        n->val = val;
        n->next = NULL;
        *head = n;
        *tail = n;
}

void append_chain_tail(Node **head,Node **tail,int val)
{
    Node *n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->next = NULL;
    Node *p = *head;
    (*tail)->next = n;
    *tail = n;
}

void append_chain_bl(Node **head,int val)
{
    Node *n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->next = NULL;
    Node *p = *head;
    while(p->next!=NULL)
        p = p->next;
    p->next = n;
}

void prepend_chain(Node **head,int val)
{
    Node *n = (Node*)malloc(sizeof(Node));
    n->val = val;
    n->next = *head;
    *head = n;
}

void print_chain(Node **head)
{
    Node *p = *head;
    while(p !=NULL)
    {
        printf("%d\n",p->val);
        p = p->next;
    }

}

void free_chain(Node **head)
{
    Node *p = *head;
    while(p !=NULL)
    {
        Node *q = p;
        p = p->next;
        free(q);
    }
}

int main()
{
    Node *head = NULL;
    Node *tail = NULL;
    create_chain(&head,&tail,10);
    append_chain_tail(&head,&tail,34);
    append_chain_bl(&head,100);    
    prepend_chain(&head,2000);
    print_chain(&head);
    free_chain(&head);
}
