//DOM(Document object model), BOM(Browser)
/*//Dom represent the page content as Html
console.log(window);
console.log(document); //Document is JS representation
console.log(document.body);
console.log(document.body.style.background = "Green");

//Bom is alert prompt
let runagain = true;
while(runagain){
let age = prompt("Enter your age"); //Input jaile string ma huncha
age = Number.parseInt(age);

const Drive = (age)=>{
  return age>=18
}

if(Drive(age)){
    alert("You can drive");
}
else{
    alert("You can't drive")
}
runagain = confirm("Do you want to play again?")
}*/

//Walking the DOM
/*  //write this in any website console
document.head; 
document.documentElement; 
document.title="CODE-SLEEP-Repeat"

let b = document.body
console.log(b.firstChild)//frist child is text becoz <body> pasi white space cha
console.log(b.firstElementChild)// yesma comment, white space hudaina
console.log(b.lastChild)
console.log(b.childNodes)
 // childNodes is a acollection not array to convert array 
 let arr = Array.from(document.body.childNodes)
 console.log(arr)*/

 //SetTimeout, Setinterval
/* const sum = (a,b) => {
  console.log("Yes I am running " + (a + b))
}

setTimeout(sum, 2000, 1, 2)
let a = setTimeout(function(){
  alert ("Settimeout")
},5000)

let b = prompt("Do you want to run timeout (y/n)?")
if(b == 'n'){
  clearTimeout(a)
}

setInterval(function(){
  alert("setinterval")
},3000)*/


