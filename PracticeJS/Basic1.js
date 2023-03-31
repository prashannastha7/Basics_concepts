//Loops
/*let marks = {
    harry : 90,
    ram : 98,
    hari : 65,
    sita: 85
}

for (let i = 0; i<Object.keys(marks).length;i++){
    console.log("The marks of " + Object.keys(marks)[i] + " are " + marks[Object.keys(marks)[i]])
}

//for in 
for(let key in marks){
       console.log("The marks of " + key + " are " + marks[key])
}

//While
let cn = 69;
let i;
while (i != 69) {
    i = prompt("Enter a number");
    console.log("Try again")
}
console.log("You have entered correct numbers")
*/

//Function
/*function math(x,y){
    return Math.round(1 +(x+y)/2);
}

const hello = ()=>{
    console.log("Hello Prashanna");
}

let a = 1, b = 2, c = 3;
hello();
console.log("one plus avg of a and b is ", math(a,b));
console.log("one plus avg of c and b is ", math(b,c));
console.log("one plus avg of a and c is ", math(a,c));
*/

//Template literals
/*let boy1 = "Ram";
let boy2 = "Hari";
let sentence = `${boy1} is a friend of ${boy2}`;
console.log(sentence);
*/

//String
/*let name = "Prashanna"
console.log(name[0])
console.log(name.length)
console.log(name.toUpperCase())
console.log(name.toLowerCase())
console.log(name.slice(2,4))
console.log(name.slice(2))
console.log(name.replace("na", "nnna"))

let friend = "Hari";
console.log(name.concat("is a friend of ", friend))
*/

//Array: diff data types
/*let num = [1, 2, 66, 95, 85]
let num1 = [5, 23, 55, 62]
let c = num.join("_");
console.log(num.pop(), num);
console.log(num.push(5), num);
console.log(num.shift(), num); //pop first element

delete num[1];
console.log(num); //delete pasi pani lenght number same huncha

let new_num = num.concat(num1);
console.log(new_num);

let compare = (a,b)=>{
    return b-a;
}
let no=[542, 23, 5, 15, 95, 2, 1, 6897]
console.log(no.sort(compare));

let number = [542, 23, 5, 15, 95, 2, 1, 6897]
number.splice(2, 3, 1021, 1022, 1564) // first 2 pasi ko element add huncha 
console.log(number)
*/

//Loop with Array
/*let a =[3,6,8,9,55]

for(let i =0;i<a.length;i++){
    console.log(a[i])
}

  //Foreach loop -> calls a func, once for each array element.
a.forEach((Element) => {
    console.log(Element *Element)
})

  //Array.from
let name = "Shyam"
let arr = Array.from(name)
console.log(arr);

  //for... of
for (let item of a){
    console.log(item)
}  

  //for... in
  for (let i in a){
    console.log(i)
}  
*/

//Map(creates new array on each array element), Reduce, Filter
/*  //Difference of map and for each is that map create new array and foreach is the loop that iterate 
let arr = [55, 69, 96]
let a = arr.map((value, index, array )=> {
    console.log(value, index, array)
    return value + index
})  
console.log(a);

  //filter
let arr2 = [45, 56, 69, 89, 2, 3, 6]
let a2 = arr2.filter((x) => {
    return x < 10
})  
console.log(a2, arr2)

  //reduce
let arr3 = [1, 2, 3, 4, 8, 9]
let y = arr3.reduce((h1, h2)=> {
    return h1+ h2
})
console.log(y)
*/