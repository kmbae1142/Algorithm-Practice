#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
	int num;
	struct node* prevNode;
	struct node* nextNode;
}Node;

typedef struct doublyList {
	Node* head;
	Node* tail;
	int cnt;
}Deque;

Deque* make_deque() 
{
	Deque* dq = (Deque*)malloc(sizeof(Deque));

	dq->head = (Node*)malloc(sizeof(Node));
	dq->tail = (Node*)malloc(sizeof(Node));
	dq->cnt = 0;

	dq->head->prevNode = NULL;
	dq->head->nextNode = dq->tail;
	dq->tail->prevNode = dq->head;
	dq->tail->nextNode = NULL;

	return dq;
}

void push_front(Deque* dq, int X) 
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	Node* nextNode = dq->head->nextNode;

	newNode->num = X;

	dq->head->nextNode = newNode;
	newNode->prevNode = dq->head;
	newNode->nextNode = nextNode;
	nextNode->prevNode = newNode;

	dq->cnt++;
}

void push_back(Deque* dq, int X)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	Node* prevNode = dq->tail->prevNode;

	newNode->num = X;

	dq->tail->prevNode = newNode;
	newNode->nextNode = dq->tail;
	newNode->prevNode = prevNode;
	prevNode->nextNode = newNode;

	dq->cnt++;
}

int pop_front(Deque* dq)
{	
	int ret = -1;

	if (dq->cnt > 0) 
	{
		Node* head = dq->head;
		Node* delNode = head->nextNode;
		ret = delNode->num;
	
		head->nextNode = delNode->nextNode;
		delNode->nextNode->prevNode = head;
		free(delNode);

		dq->cnt--;
	}

	return ret;
}

int pop_back(Deque* dq) 
{
	int ret = -1;

	if (dq->cnt > 0) 
	{
		Node* tail = dq->tail;
		Node* delNode = tail->prevNode;
		ret = delNode->num;

		tail->prevNode = delNode->prevNode;
		delNode->prevNode->nextNode = tail;
		free(delNode);

		dq->cnt--;
	}

	return ret;
}

void clear_all(Deque* dq) 
{
	while (dq->cnt > 0) 
	{
		Node* head = dq->head;
		Node* delNode = head->nextNode;

		head->nextNode = delNode->nextNode;
		delNode->nextNode->prevNode = head;

		free(delNode);
		dq->cnt--;
	}

	free(dq);
}

int main() {

	int N;
	scanf("%d", &N);
	Deque* dq = make_deque();

	while (N--) {
		char str[15];
		int X;
		scanf("%s", str);

		if (!strcmp(str, "push_front")) {
			scanf("%d", &X);
			push_front(dq, X);
		}
		else if (!strcmp(str, "push_back")) {
			scanf("%d", &X);
			push_back(dq, X);
		}
		else if (!strcmp(str, "pop_front")) {
			printf("%d\n", pop_front(dq));
		}
		else if (!strcmp(str, "pop_back")) {
			printf("%d\n", pop_back(dq));
		}
		else if (!strcmp(str, "size")) {
			printf("%d\n", dq->cnt);
		}
		else if (!strcmp(str, "empty")) {
			printf("%d\n", (dq->cnt == 0));
		}
		else if (!strcmp(str, "front")) {
			printf("%d\n", (dq->cnt > 0) ? dq->head->nextNode->num : -1);
		}
		else if (!strcmp(str, "back")) {
			printf("%d\n", (dq->cnt > 0) ? dq->tail->prevNode->num : -1);
		}
	}

	clear_all(dq);
	return 0;

}