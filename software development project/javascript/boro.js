var numbers = [1,3,5,11,21,54,69];
var largestnumber = numbers[0];
for(var i=0;i<numbers.length;i++){
    var element = numbers[i];
    if(element>largestnumber){
        largestnumber = element;
    }
}
console.log(largestnumber);