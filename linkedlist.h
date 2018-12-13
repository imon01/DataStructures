#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_


typedef struct  LinkedList_* LinkedList;

LinkedList malloc_ll(void);
void free_ll( LinkedList);

int add_ll( LinkedList, int);
int search_ll( LinkedList, int);
int delete_ll( LinkedList , int);
void reverse_ll(LinkedList);
void lazymerge_ll(LinkedList, LinkedList);
void append_ll(LinkedList, LinkedList);

#endif
