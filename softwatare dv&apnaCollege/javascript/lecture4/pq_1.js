let marks = [99, 88 , 78, 98, 54];
let sum = 0;
for ( let val of marks){
    sum+=val;   
}
let avg = sum / marks.length;
console.log(`Avarage marks of the class = ${avg}`);