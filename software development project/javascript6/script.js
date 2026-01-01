let chec = document.getElementsByTagName("h1");
console.log(chec);

let title = document.getElementById("title").style.color="red";
document.getElementById("title").style.removeProperty("color");
console.log(title);

let child = document.getElementsByClassName("child");
console.log(child[1]);

let img = document.getElementById("img");
img.setAttribute("alt","Profile picture");
console.log(img.getAttribute("alt","Profile Picture"));

img.classList.add("testClass");
console.log(img);

let hero = document.getElementById("hero");
console.log(hero.innerText);

let input =document. getElementById("input").value;
console.log(typeof(input));

let parent = document.getElementById("parent").innerHTML;
console.log(parent);

let testDiv = document.getElementsByClassName("test");
console.log(testDiv[0].childNodes[1].parentNode .parentNode.parentElement.childNodes[5])