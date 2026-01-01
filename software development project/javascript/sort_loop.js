var arr = [1,11,9,8,7,4,2,3,5,6,10];
for(var i =0;i<arr.length;i++){
    for(var j=0;j<arr.length-i-1;j++){
        if(arr[j]>arr[j+1]){
            var tmp=arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=tmp;
        }
    }
}
console.log(arr);