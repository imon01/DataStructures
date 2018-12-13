#include "array_list.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>


#define DEFAULT_LIST_SIZE 32 
#define DEFAULT_BLOCK_SIZE 32 
#define init_arraylist(...) __init_call__( (defualts) {__VA_ARGS__});


typedef unsigned long u_long
typedef unsigned char u_char



typedef struct
{
	size_t list_size;
	size_t block_size;
} defualts;



//linking array nodes
typedef struct array_block
{
	enum space {FULL=0,FREE};	
	size_t 	cells;	
	size_t 	units_count;
	size_t	mem_size; 
	size_t	datum_size	
	array_block * next;
	void ** array;
}array_block;



//Holds entire data structure information
typedef struct array_list
{
	u_long list_size;		//global array_list size
	u_long block_count; 	//size of unit storage
	size_t block_size;		//array_block size	
	array_block* head;		//head of array_node
};

//initializes variables
static array_list* __init_call__(defaults args)
{

	size_t l_size = args.list_size ? args.list_size: L;
	size_t b_size = args.block_size ? args.block_size: B;

	//should call init_list
	return __init__( l_size, b_size);
}



static 

//
//WARNING: check for size_t * multiplication overflow
array_list* init_list(size_t list_size)
{
	array_list* a 	= malloc(sizeof(array_list));
	a->list_size 	= 0;
	a->block_count	= 1;
	a->block_size 	= DEFAULT_BLOCK_SIZE;
	a->head = init_block(DEFAULT_BLOCK_SIZE);
	
	list_size -= a->block_size;
	
	while(list_size)
	{
		//TODO: init array_blocks
		a->head
	}
	return a;
}

//TODO
array_list* init_list(size_t list_size, size_t block_size)
{
	array_list* a = malloc(sizeof(array_list));
	a->list_size 	= 0;
	a->block_count	 = 1;	
	a->head = init_block(block_size);
	return a;
}


static array_block * init_block(size_t block_size, size_t datum_size)
{
	array_block * b = malloc( sizeof( array_block) );


	if( array_block == null)
	{ 	
		goto ERROR;
	}	

	b->cells		= block_size;
	b->space 		= FREE;	
	b->units_count	= 0;

	//Check for overflow or too large of value
	b->mem_size 	= block_size* sizeof(void*);
	b->datum_size	= datum_size;
	b->next			= null;	
	b->array		= malloc( b->mem_size + 1);

	//TODO: check for errors here	
	assert(b->array);
	b->array[cells] = null;

	return b;	
}


//TODO
int add(array_list * list, void* datum)
{
	array_block* temp_block = list->head;

	//check for available space	in start block, insert if yes
	while( temp_block && !temp_block->space )
	{
		temp_block = temp_block->next;	
	}	

	temp_block->array[ temp_block->units_count++ ] = datum;
	
	if( temp_block->units_count == temp_block->cells)
	{
		temp_block->space = FULL;
		temp_block->next = init_block( DEFAULT_BLOCK_SIZE);
		list->blocks_count++;				
	}

	return 1;
} 






int delete(array_list * list, int index)
{
	int array_index = list->list_size - index;
	int value = 1;
	array_block * temp_block = list->head;	
	void ** array;
	
	if( index < 0 && index > list->list_size)
	{
		goto ERROR_DELETE;
	}
	
	while(temp_block)
	{
		if(index < temp_block->cells)
		{
			array  = temp_block->array;
			array[index] = null;		
		}
		else
		{
			temp_block = temp_block->next;	
		}

	}


	ERROR_DELETE:
		fprintf(stderr, "index out of bounds");
		value = 0;
	
	return value;
	
} 



