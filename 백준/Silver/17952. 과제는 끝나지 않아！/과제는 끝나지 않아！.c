#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
	int score, min;
	struct node* nextNode;
}Node;

typedef struct linkedList {
	int size;
	Node* head;
}Stack;

Stack* make_stack() 
{
	Stack* st = (Stack*)malloc(sizeof(Stack));

	st->head = (Node*)malloc(sizeof(Node));
	st->head->nextNode = NULL;
	st->size = 0;

	return st;
}

void push(Stack* st, int score, int min) 
{	
	Node* head = st->head;
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->score = score;
	newNode->min = min;

	newNode->nextNode = head->nextNode;
	head->nextNode = newNode;

	st->size++;
}

void pop(Stack* st) 
{
	Node* head = st->head;
	Node* delNode = head->nextNode;

	head->nextNode = delNode->nextNode;
	free(delNode);

	st->size--;
}

void clear_all(Stack* st) 
{
	Node* current = st->head;

	while (current != NULL)
	{
		Node* next = current->nextNode;
		free(current);
		current = next;
	}

	free(st);
}

int main() {

	Stack* st = make_stack();
	int N, _case, sum = 0;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		int score, min;
		scanf("%d", &_case);
		if (_case) {
			scanf("%d %d", &score, &min);
			if (min == 1) {
				sum += score;
			}
			else {
				push(st, score, min - 1);
			}
		}
		else {
			if (st->size > 0) {
				Node* top = st->head->nextNode;
				top->min--;
				if (top->min == 0) {
					sum += top->score;
					pop(st);
				}
			}
		}
	}

	printf("%d", sum);
	clear_all(st);

}