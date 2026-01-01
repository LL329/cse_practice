// loops of js
let newTing = "newStringLearning";
let sz = 0;
for (let val of newTing){
    console.log("Val =",val);
    sz++;
}
console.log("sz =",sz);


// loops in js -> objects
let student = {
    names : "Rahul Kumar",
    age : 20,
    cgpa : 7.5,
    isPass : true,
};

for(let key in student){
    console.log("key=", key, " value=", student[key]);
}
