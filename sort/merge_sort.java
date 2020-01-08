class merge_sort{
    public static void sort(int[] array, int left, int right){
        if (left < right){
            int mid = (left+right-1)/2;
            sort(array, left, mid);
            sort(array, mid+1, right);
            merge(array, left, mid, right);
        }
    }

    public static void merge(int[] array, int left, int mid, int right){
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] leftSubArray = new int[n1];
        int[] rightSubArray = new int[n2];

        for(int i=0; i<n1; i++){
            leftSubArray[i] = array[left+i];
        }

        for(int i=0; i<n2; i++){
            rightSubArray[i] = array[mid+i+1];
        }

        int i=0;
        int j=0;
        int k=left;
        
        while(i < n1 && j < n2){
            if (leftSubArray[i] <= rightSubArray[j]){
                array[k] = leftSubArray[i];
                i = i+1;
            }
            else{
                array[k] = rightSubArray[j];
                j = j+1;
            }
            k = k+1;
        }

        while(i < n1){
            array[k] = leftSubArray[i];
            i = i+1;
            k = k+1;
        }

        while(j < n2){
            array[k] = rightSubArray[j];
            j = j+1;
            k = k+1;
        }
    }


    public static void main(String args[]){
        int[] array = {5, 3, 2, 4, 8, 1};
        sort(array, 0, array.length-1);
        for(int i=0; i<array.length; i++){
            System.out.print(array[i]+" ");
        }
        System.out.println();
    } 
}