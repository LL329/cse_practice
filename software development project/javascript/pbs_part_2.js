var frinds = ["rahim","karim","abul","salam","heroAlom"];
var largestName = frinds[0];
for(var i=0;i<frinds.length;i++){
    var element = frinds[i];
    if(element.length>largestName.length){
        largestName = element;
    }
}
console.log(largestName);