#include <stdio.h>
#include <stdlib.h>

int *arr = NULL;

typedef enum {
	false = 0, 
	true = 1
} boolean;

void alloc_array(int n) {
	arr = (int *) malloc(sizeof(int)*n);
	int i;
	for(i=0;i<n;i++) {
		arr[i] = 0;
	}
}

void dealloc_array() {
	free(arr);
	arr = NULL;
}

boolean backtrack_function(int x, int array_size) {

	int i;
	if(x==0) {
		return true;
	}
	for(i=0; i < array_size;i++) {
		if((i+x+1) >= array_size) {
			return false;
		}
		if(arr[i] == 0 && arr[i+x+1] == 0) {
			arr[i] = x;
			arr[i+x+1] = x;
			if(backtrack_function(x-1, array_size) == true) {
				return true;
			}
			arr[i] = 0;
			arr[i+x+1] = 0;
		}
	}
	return false;
}

void print_array(int array_size) {
	int i;
	printf("\n{");
	for(i=0;i< array_size-1; i++) {
		printf(" %d,", arr[i]);
	}
	printf(" %d }\n", arr[i]);
}

int pair_shift_numbers_main(int n) {
	
	alloc_array(2*n);
	
	if(backtrack_function(n, 2*n) == true) {
		printf("Solution: \n");
		print_array(2*n);
	}
	else {
		printf("No Solution\n");
	}
	
	dealloc_array();
}

int main(char **argv, int argc) {
	int n;
	printf("Enter value n:");
	scanf("%d", &n);
	pair_shift_numbers_main(n);
}
