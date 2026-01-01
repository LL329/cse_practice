let num = [1, 2, 3, 4, 5, 6, 7];
//slice()
console.log(num.slice(1,3)); //st end, end if i give 2 coming 1
// full array coppy
console.log(num.slice());


// splice()

num.splice(2, 2, 101, 102 , 1099,520); //st 2 index thake , 2 number index jaw 2 ta delete koro , new add korbo koida
console.log(num)

//add element 
num.splice(0,0,101); // koi num index ee add hobe st = 0, delete na korla  = 0, add element number 101 
console.log(num);


// delete element
num.splice(3,1); // 3 number element ee jaw, delate kro.
