var numbers = [1,2,3,3,4,4,5,6,7,8,9,10];
var unique = [];

for(var i = 0; i < numbers.length; i++){
    var element = numbers[i];
    if(unique.indexOf(element) === -1){ 
        unique.push(element); 
    }
}

console.log(unique); 
// Output: [1,2,3,4,5,6,7,8,9,10]
