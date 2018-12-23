#include "linkedlist.h"

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>


typedef struct node_t_* node_t;

typedef struct node_t_ 
{
	int value;
	node_t next;
}node_t_;


typedef struct linkedlist_t_ 
{
	node_t root;
	node_t tail;
	int size;
}linkedlist_t_;

/*----------------------------------*/
/*Local prototypes*/


void __test_linked_list__(void);
void __clean__(linkedlist_t l);
void __test_iter_LL__(linkedlist_t l);
void __test_add_LL__(linkedlist_t l);
void __test_search_LL__(linkedlist_t l, int val);
void __test_repop_LL__(linkedlist_t l, int i, int j);
void __test_delete_LL__(linkedlist_t l, int i, int j);
void __test_reverse_LL__(linkedlist_t l);
void __test_merge_LL(linkedlist_t la, linkedlist_t lb);
void __test_append_LL(linkedlist_t la, linkedlist_t lb);
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
	linkedlist_t l = malloc_ll();
//	linkedlist_t l2 = malloc_ll();
	fprintf(stderr, "malloc_ll: passed\n");

	__test_add_LL__(l);
	add_ll(l, 100);
	__test_iter_LL__(l);
//	__test_delete_LL__(l, 0,2);
	delete_ll(l, 0);
//	for(int i = 0; i < 10; i++)
//		__test_search_LL__(l, i);
//	
//	for(int i = 55; i < 62; i++)
//		add_ll(l2, i);	
//
//	add_ll(l, 100);
//	add_ll(l2, 999);
//	__test_search_LL__(l, -1);
//	__test_delete_LL__(l, 0,1);
//	__test_iter_LL__(l);
//	__test_delete_LL__(l, 2,7);
//	__test_iter_LL__(l);
//	__test_repop_LL__(l, 107, 113);
//	__test_iter_LL__(l);
//	__test_reverse_LL__(l);


	__test_iter_LL__(l);
//	__test_iter_LL__(l2	);
//	__test_append_LL(l, l2);	

//	lazymerge_ll(l, l2);
//	__test_iter_LL__(l);
//	__test_iter_LL__(l2);
//	
	printf("Final LL size: %d\n", l->size);
	__clean__(l);
///	__clean__(l2);
}

void __test_repop_LL__(linkedlist_t l, int i, int j)
{
	while( i < j)
		add_ll(l, i++);
	
}

void __test_iter_LL__(linkedlist_t l)
{
	node_t curr = l->root;
	while( curr)
	{
		printf("%d ", curr->value);
		curr = curr->next;
	}

	printf("\n");
}

void __test_add_LL__(linkedlist_t l)
{
	int i  = 0;
	for(; i < 10; i++)
	{
		add_ll(l, i);
	}
}	

void __test_search_LL__(linkedlist_t l, int val)
{
	fprintf(stderr,"searching: %d, %s\n",val,(search_ll(l, val) == -1)?"not found":"found");
 
}

void __test_delete_LL__(linkedlist_t l, int i, int j)
{
		while( i< j)	
			delete_ll(l, i++);
}

void __test_reverse_LL__(linkedlist_t l)
{
	reverse_ll(l);
}

void __test_append_LL(linkedlist_t la, linkedlist_t lb)
{
	append_ll(la, lb);
}

void __clean__(linkedlist_t l)
{
	node_t c = l->root;
	node_t t = 0;

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

linkedlist_t malloc_ll(void)
{
	linkedlist_t list = (linkedlist_t) malloc( sizeof(list));

	if( list == 0)
	{
		perror("malloc: failed linkedlist_t creation");
	}
	return list;
}

int add_ll( linkedlist_t list, int value)
{
	node_t n = (node_t ) malloc( sizeof(n));
	if(n  == 0)
	{
		perror("malloc: failed add_ll new node_t");
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

void free_ll(linkedlist_t list)
{
	//Copy __clean__ here
	return;
}

int search_ll( linkedlist_t list, int value)
{
	node_t curr = list->root;
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

int delete_ll( linkedlist_t list, int value)
{


	node_t indirect = list->root;
	node_t target = 0;
	node_t* save = &indirect;

	while(indirect)
//	while( (*indirect)->value != value)
	{
		target = indirect;
		if( indirect->value == value)
		{
			break; 
		
		}	
		indirect = indirect->next;
	}
	list->size--;
	indirect = indirect->next;	
	list->root = *save;
	free(target);	

	return 0;	
}

void reverse_ll( linkedlist_t list)
{
	node_t prev = 0;
	node_t curr = list->root;

	node_t sto = 0;

	while(curr)
	{
		sto = curr->next;
		curr->next = prev;
		prev = curr;
		curr = sto;
	}
	
	list->root = prev;
}


void append_ll( linkedlist_t list, linkedlist_t list2)
{
	if(list2 == NULL)
		return;

	list->tail->next = list2->root;
	list->tail = list2->tail;
	list2->root = 0;
	list->size += list2->size;
	list2->size = 0;

	free(list2);
}


void lazymerge_ll(linkedlist_t list, linkedlist_t list2)
{
	if( list2 == NULL)
		return;

	node_t right = list2->root, prev = list->root, sto = 0;


	
	node_t left = list->root->next;

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

void sort_ll(linkedlist_t l)
{
	//TODO: implement
//	node_t curr = l->root, max = 0;
//
//	int max = curr->value;
//	curr = curr->next;
//
//	while(curr)	
//	{
//		if( curr->value > max->value)
//		{
//			max = curr;
//		}
//		curr = curr->next;
//	}
} 
