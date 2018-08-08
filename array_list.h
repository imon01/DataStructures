


typedef struct defualt;
typedef struct array_block;
typedef struct array_list;


array_list  * init_list(size_t);
static array_block * init_block(size_t);


int add(array_list, void*);
int delete(array_list, void*);




