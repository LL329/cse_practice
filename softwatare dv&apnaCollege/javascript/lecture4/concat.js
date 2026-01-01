let marvel_heroes = ["thor", "spider", "ironman","kurkuri begum", "kulkula khatun"];
let dc_heroes = ["superman", "batman"];
let surman_heroes = ["joblu", "koblu", "moblu"];


// add value at last
dc_heroes.push("dogy saheb");
console.log(dc_heroes);


// remove value at last 
marvel_heroes.pop();
console.log(marvel_heroes);



// add values in first
surman_heroes.unshift("sucurita");
console.log(surman_heroes);


// remove values in first
marvel_heroes.shift();
console.log(marvel_heroes);


//add multiples array 
let mutual_heroes = marvel_heroes.concat(dc_heroes ,surman_heroes);
console.log(mutual_heroes);
