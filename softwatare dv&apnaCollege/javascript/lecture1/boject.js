//Data types in js
// 1.primitive (7) Number,string,Boolean,Undefined,Null,BigInt,Symbol
//2.Non-primitive(1) objects->1.Array 2.Function
//objects is a collection of values . {key:value}
// const objects key can be update
// let can update , const can't be update
const student = {
    fullName : "Md.Abdur Rohman",
    age : 20,
    cgpa : 8.2,
    isPass: true

};
student["age"] = student["age"] + 9 ;
student["fullName"] = "Dildar comidean";
student["cgpa"] = student["cgpa"] + 2;
console.log(student.age);
console.log(student["cgpa"]);
console.log(student.fullName);