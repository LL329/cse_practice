// 1.Problem number check number Even or Odd
var n=0;
if(n%2==1){
    console.log("It's Odd Number")   
}
else if(n==0){
    console.log("This is zero");
}
else{
    console.log("It's Even Number");
}

//2.Give you a array 1-20 digits you have to reverse it
var arr=[2,5000,3,5,11,17,14,16,1000,2000,210,1900,1200,19,18,1,4,100,99,98,85,31,49,39,29,79,69,6,8,9,10];
// console.log(arr.reverse());
console.log(arr.length)
console.log(arr.sort(function(a,b){return a - b}));
console.log(arr.reverse())