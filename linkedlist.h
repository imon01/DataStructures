#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_


typedef struct  linkedlist_t_* linkedlist_t;

linkedlist_t malloc_ll(void);
void free_ll( linkedlist_t);

int add_ll( linkedlist_t, int);
int search_ll( linkedlist_t, int);
int delete_ll( linkedlist_t , int);
void reverse_ll(linkedlist_t);
void lazymerge_ll(linkedlist_t, linkedlist_t);
void append_ll(linkedlist_t, linkedlist_t);

#endif
