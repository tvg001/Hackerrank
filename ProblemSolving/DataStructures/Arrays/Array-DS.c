int* reverseArray(int a_count, int* a, int* result_count) {
    int * array = (int *)malloc(sizeof(int)*a_count);


   for(int i=a_count-1;i>=0;i--){
       array[a_count-i-1]=a[i];
   }
   *result_count = a_count;
   return array;
}
