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

//Promises -> 
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