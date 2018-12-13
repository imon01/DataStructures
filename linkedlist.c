#include "linkedlist.h"

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>


typedef struct node_* node;

typedef struct node_ 
{
	int value;
	node next;
}node_;


typedef struct LinkedList_ 
{
	node root;
	node tail;
	int size;
}LinkedList_;

/*----------------------------------*/
/*Local prototypes*/


void __test_linked_list__(void);
void __clean__(LinkedList l);
void __test_iter_LL__(LinkedList l);
void __test_add_LL__(LinkedList l);
void __test_search_LL__(LinkedList l, int val);
void __test_repop_LL__(LinkedList l, int i, int j);
void __test_delete_LL__(LinkedList l, int i, int j);
void __test_reverse_LL__(LinkedList l);
void __test_merge_LL(LinkedList la, LinkedList lb);
void __test_append_LL(LinkedList la, LinkedList lb);
/*----------------------------------*/
/*----------------------------------*/


int main(int argc, char* argv)
{

	__test_linked_list__();

	return 0;
}

/*----------------------------------*/
/*---------Testing functions--------*/
void __test_linked_list__(void)
{
	LinkedList l = malloc_ll();
	LinkedList l2 = malloc_ll();
	fprintf(stderr, "malloc_ll: passed\n");

	__test_add_LL__(l);
	__test_iter_LL__(l);
	
//	for(int i = 0; i < 10; i++)
//		__test_search_LL__(l, i);
	
	for(int i = 55; i < 62; i++)
		add_ll(l2, i);	

	add_ll(l, 100);
	add_ll(l2, 999);
	__test_search_LL__(l, -1);
//	__test_delete_LL__(l, 0,1);
//	__test_iter_LL__(l);
//	__test_delete_LL__(l, 2,7);
//	__test_iter_LL__(l);
//	__test_repop_LL__(l, 107, 113);
//	__test_iter_LL__(l);
//	__test_reverse_LL__(l);


	__test_iter_LL__(l);
	__test_iter_LL__(l2	);
//	__test_append_LL(l, l2);	

	lazymerge_ll(l, l2);
	__test_iter_LL__(l);
	__test_iter_LL__(l2);
	
	printf("Final LL size: %d\n", l->size);
	__clean__(l);
	__clean__(l2);
}

void __test_repop_LL__(LinkedList l, int i, int j)
{
	while( i < j)
		add_ll(l, i++);
	
}

void __test_iter_LL__(LinkedList l)
{
	node curr = l->root;
	while( curr)
	{
		printf("%d ", curr->value);
		curr = curr->next;
	}

	printf("\n");
}

void __test_add_LL__(LinkedList l)
{
	int i  = 0;
	for(; i < 10; i++)
	{
		add_ll(l, i);
	}
}	

void __test_search_LL__(LinkedList l, int val)
{
	fprintf(stderr,"searching: %d, %s\n",val,(search_ll(l, val) == -1)?"not found":"found");
 
}

void __test_delete_LL__(LinkedList l, int i, int j)
{
		while( i< j)	
			delete_ll(l, i++);
}

void __test_reverse_LL__(LinkedList l)
{
	reverse_ll(l);
}

void __test_append_LL(LinkedList la, LinkedList lb)
{
	append_ll(la, lb);
}

void __clean__(LinkedList l)
{
	node c = l->root;
	node t = 0;

	while( c )
	{
		t = c->next;
		free(c);
		c = t;
	}

	fprintf(stderr, "__clean__: passed\n");
}
/*-----------------------------*/
/*--------LL Features----------*/

LinkedList malloc_ll(void)
{
	LinkedList list = (LinkedList) malloc( sizeof(list));

	if( list == 0)
	{
		perror("malloc: failed LinkedList creation");
	}
	return list;
}

int add_ll( LinkedList list, int value)
{
	node n = (node ) malloc( sizeof(n));
	if(n  == 0)
	{
		perror("malloc: failed add_ll new node");
	}

	n->value = value;
	n->next = 0;
	list->size++;
	
	if( list->root == 0)
	{
		//if root is NULL, so is tail	
		list->root = n;
		list->tail = n;
		return 0;
	}
	
	list->tail->next = n;
	list->tail = n;

	return 0;	
}

void free_ll(LinkedList list)
{
	//Copy __clean__ here
	return;
}

int search_ll( LinkedList list, int value)
{
	node curr = list->root;
	int index = 0;
	
	while( curr )
	{
		if( curr->value == value)
		{
			return index;
		}
		index++;
		curr = curr->next;	
	}
	return -1;	
}

int delete_ll( LinkedList list, int value)
{
	node curr = list->root;
	node prev = 0;
	if( curr->value == value)
	{
		list-> root = list->root->next;
		list->size--;	
		free(curr);
		return 0;
	}

	while( curr )
	{
		if( curr->value == value)
		{
			prev->next= curr->next;
			break;
		}
		prev = curr;
		curr = curr->next;	
	}

	if( curr != NULL)	
	{
		free(curr);	
		list->size--;
	}
	return 0;	
}

void reverse_ll( LinkedList list)
{
	node prev = 0;
	node curr = list->root;

	node sto = 0;

	while(curr)
	{
		sto = curr->next;
		curr->next = prev;
		prev = curr;
		curr = sto;
	}
	
	list->root = prev;
}


void append_ll( LinkedList list, LinkedList list2)
{
	if(list2 == NULL)
		return;

	list->tail->next = list2->root;
	list->tail = list2->tail;
	list2->root = 0;
	list->size += list2->size;
	list2->size = 0;
}


void lazymerge_ll(LinkedList list, LinkedList list2)
{
	if( list2 == NULL)
		return;

	node right = list2->root, prev = list->root, sto = 0;


	
	node left = list->root->next;

	if( prev->value > right->value)
	{
		list->root = list2->root; 
		left = prev;
		prev = right;
		right = right->next;
	}
	
	//while( merging): 
	while(1)
	{

		if( left->value > right->value)
		{
			prev->next = right;
			prev = right; 
			right = right->next;
		
			if(right == NULL)
				break;
		}
		else
		{
			prev->next = left;
			prev = left;
			left = left->next;
			if( left == NULL)
				break;
		}
	}
	//edge case: 1 left remaining
	
	prev->next = left;
	if( left == NULL)
	{
		prev->next = right;
	}

	list->size += list2->size;
	list2->root = 0;
}

void sort_ll(LinkedList l)
{

	node curr = list->root;
} 
