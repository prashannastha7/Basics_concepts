//Callback function -> is a function passed into another function as an argument, which is then invoked inside the outer function to complete an action
/*function myDisplayer(some) {
    document.getElementById("demo").innerHTML = some;
  }
  
  function myCalculator(num1, num2, myCallback) {
    let sum = num1 + num2;
    myCallback(sum);
  }
  
  myCalculator(5, 5, myDisplayer);

// In the example below, myFunction is used as a callback.
//myFunction is passed to setTimeout() as an argument.

setTimeout(myFunction, 3000);

function myFunction() {
  document.getElementById("demo").innerHTML = "I love You !!";
}*/

//Promises
/* //Basics 
let promise = new Promise((resolve, reject) => {
    alert("Hello")
    resolve(69)
})

console.log("hello 1")
setTimeout(() => {
    console.log("Hello 2")
}, 2000);

console.log("hello 3")
console.log(promise)

//then() catch()
let p1 = new Promise((resolve, reject) => {
          console.log("Promise is pending")
          setTimeout(() => {
            resolve(true)
          },4000)    
})

let p2 = new Promise((resolve, reject) => {
  console.log("Promise is pending")
  setTimeout(() => {
    reject(new Error("I am an Error"))
  },4000)
})

// To get value
p1.then((value) => {
  console.log(value)
})

//To catch errors
p2.catch((error) => {
  console.log("error occured in p2")
})

//combine
p2.then((value)=>{
  console.log(value)
}, (error) => {
  console.log(error)
})

//chaining 
let s1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log("Resolved after 2 sec")
    resolve(7)
  }, 2000);
})

s1.then((value) => {     //value 7 yesma huncha aani,
  console.log(value)
  return new Promise((resolve, reject) => {   //yesle naya value muni pass garcha  
    setTimeout(() => { resolve("Promise 2")
  },2000)
}).then((value) => {   //yesle value paya pasi Done print huncha
  console.log("Done")
  return 2
}).then((value)=> {
  console.log("Final")
})
})


//multiple handlers
let r1 = new Promise((resolve, reject) => {
  alert("Hey not resolved")
  setTimeout(() => {
    resolve(1);
  }, 2000)
})

r1.then(() => {
  console.log("This is resolved now")
})

.then(() => {
  console.log("Huurrraaayyyyy")
})
*/

//Promises API
